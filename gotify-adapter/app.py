from flask import Flask, request, jsonify
import requests
import os

# Cache last known values per alertname + region
LAST_VALUES = {}

DELTA_ALERT_KEYWORDS = ["Sudden", "Spike", "Delta"]

app = Flask(__name__)

GOTIFY_URL = os.getenv("GOTIFY_URL")  # e.g. http://gotify
GOTIFY_TOKEN = os.getenv("GOTIFY_TOKEN")

SEVERITY_EMOJI = {
    "critical": "🔥",
    "warning": "⚠️",
    "failure": "❌"
}

@app.route("/alert", methods=["POST"])
def alert():
    payload = request.json

    status = payload.get("status")  # firing / resolved
    alerts = payload.get("alerts", [])
    alertname = payload.get("groupLabels", {}).get("alertname", "Alert")
    is_delta_alert = any(word in alertname for word in DELTA_ALERT_KEYWORDS)

    if not alerts:
        return jsonify({"status": "ignored, no alerts"}), 200

    # Determine severity (from first alert)
    severity = alerts[0].get("labels", {}).get("severity", "warning")
    emoji = SEVERITY_EMOJI.get(severity, "⚠️")

    regions_count = len(alerts)

    # Title
    if status == "firing":
        title = f"{emoji} {alertname} ({regions_count} regions)"
    else:
        title = f"✅ {alertname} resolved ({regions_count} regions)"

    # Message body
    lines = []
    for a in alerts:
        region = a.get("labels", {}).get("region", "unknown")
        description = a.get("annotations", {}).get("description", "")
        value = a.get("valueString")

        key = f"{alertname}:{region}"

        if status == "firing" and value:
            LAST_VALUES[key] = value

        if status == "firing":
            # Store last known value
            if value:
                LAST_VALUES[key] = value

            # FIRING message
            if description:
                lines.append(f"• {region} — {description}")
            elif value:
                lines.append(f"• {region} — value {value}")
            else:
                lines.append(f"• {region} — threshold breached")

        else:
            # RESOLVED message
            cached_value = LAST_VALUES.get(key)

            if is_delta_alert:
                lines.append(f"• {region} — spike ended")
            elif cached_value:
                lines.append(f"• {region} — back to {cached_value}")
            else:
                lines.append(f"• {region} — back to normal")

    message = "\n".join(lines)

    # Send to Gotify
    response = requests.post(
        f"{GOTIFY_URL}/message?token={GOTIFY_TOKEN}",
        json={
            "title": title,
            "message": message,
            "priority": 5
        },
        timeout=5
    )

    response.raise_for_status()

    return jsonify({"status": "sent"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

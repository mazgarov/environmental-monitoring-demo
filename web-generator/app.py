from flask import Flask, render_template_string
import random
import time
import threading
import os

app = Flask(__name__)

# Configurable update interval (seconds)
DATA_UPDATE_INTERVAL = int(os.getenv("DATA_UPDATE_INTERVAL", "180"))

REGIONS = [
    "RumBulogʻi",        # spring
    "ChinSoy",           # river
    "HindShamoli",       # wind
    "SindDaryosi",       # river
    "TuronDashti",       # steppe
    "SugdBogʻi",         # garden
    "XurosonBuluti",     # cloud
    "IroqQuyoshi",       # sun
    "ShomTongʻi",        # dawn
    "MisrQuyoshi",       # sun
    "MagribShafaqi",     # sunset glow
    "AndalusBogʻi",      # garden
    "KavkazTogʻi",       # mountain
    "DehliIssigʻi",      # heat
    "TabaristonYomgʻiri",# rain
    "DaylamYeli",        # wind
    "ArmanQori",         # snow
    "GurjBuloq",         # spring
    "SaqalibaMuzligi",   # glacier/ice
    "BulgarSovugi",      # cold
    "XitoyTumanı",       # fog
    "QipchoqDashti",     # steppe
    "OguzYulduzi",       # star
    "XazarDengizi",      # sea
    "BalxBahori"         # spring season
]

state = {}
current_data = []
last_update_time = None
lock = threading.Lock()

def init_state():
    for region in REGIONS:
        state[region] = {
            "temperature": random.uniform(10, 25),
            "aqi": random.randint(30, 80),
            "co2": random.randint(400, 600),
        }

def generate_data():
    data = []

    for region in REGIONS:
        current = state[region]

        # Gradual changes
        current["temperature"] += random.uniform(-0.5, 0.5)
        current["aqi"] += random.randint(-10, 10)
        current["co2"] += random.randint(-30, 30)

        # Bounds
        current["temperature"] = max(-10, min(45, current["temperature"]))
        current["aqi"] = max(0, min(400, current["aqi"]))
        current["co2"] = max(300, min(3000, current["co2"]))

        # Rare events
        if random.random() < 0.05:
            current["aqi"] += random.randint(50, 150)

        if random.random() < 0.02:
            current["co2"] = 0

        # Status
        status = "OK"

        if current["aqi"] > 150 or current["co2"] > 1500:
            status = "WARNING"

        if current["aqi"] > 300 or current["co2"] > 2500:
            status = "CRITICAL"

        if current["co2"] == 0:
            status = "FAILURE"

        data.append({
            "region": region,
            "temperature": round(current["temperature"], 1),
            "aqi": int(current["aqi"]),
            "co2": int(current["co2"]),
            "status": status
        })

    return data

def update_data_loop():
    global current_data, last_update_time

    while True:
        new_data = generate_data()
        with lock:
            current_data = new_data
            last_update_time = time.strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(DATA_UPDATE_INTERVAL)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Environmental Monitoring</title>
    <meta http-equiv="refresh" content="60">
    <style>
        body { font-family: Arial, sans-serif; background-color: #fafafa; }
        table { border-collapse: collapse; width: 70%; margin: auto; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
        th { background-color: #eee; }
        .OK { background-color: #d4edda; }
        .WARNING { background-color: #fff3cd; }
        .CRITICAL { background-color: #f8d7da; }
        .FAILURE { background-color: #343a40; color: white; } /* dark gray / black */
        tr:hover {
            background-color: #cce5ff !important;
            cursor: pointer;
        }
    </style>
</head>
<body>

<h2 style="text-align:center;">Environmental Monitoring – Synthetic Data</h2>
<p style="text-align:center;">
    Last data update: {{ last_update }} (Asia/Tashkent)
</p>

<table>
<tr>
    <th>#</th>
    <th>Region</th>
    <th>Temperature (°C)</th>
    <th>Air Quality Index</th>
    <th>CO₂ (ppm)</th>
    <th>Status</th>
</tr>

{% for row in data %}
<tr class="{{ row.status }}">
    <td>{{ loop.index }}</td>
    <td>{{ row.region }}</td>
    <td>{{ row.temperature }}</td>
    <td>{{ row.aqi }}</td>
    <td>{{ row.co2 }}</td>
    <td>{{ row.status }}</td>
</tr>
{% endfor %}

</table>
</body>
</html>
"""

@app.route("/")
def index():
    with lock:
        data = list(current_data)
        last_update = last_update_time
    return render_template_string(
        HTML_TEMPLATE,
        data=data,
        last_update=last_update
    )

if __name__ == "__main__":
    init_state()

    # Initialize first dataset
    current_data = generate_data()
    last_update_time = time.strftime("%Y-%m-%d %H:%M:%S")

    thread = threading.Thread(target=update_data_loop, daemon=True)
    thread.start()

    app.run(host="0.0.0.0", port=8000)



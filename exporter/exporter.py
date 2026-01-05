import requests
from bs4 import BeautifulSoup
from prometheus_client import start_http_server, Gauge
import time
import os

previous_data = {}

TARGET_URL = os.getenv("TARGET_URL", "http://web-generator:8000")
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", "30"))

temperature_metric = Gauge(
    "environment_temperature_celsius",
    "Temperature per region",
    ["region"]
)

aqi_metric = Gauge(
    "environment_aqi",
    "Air Quality Index per region",
    ["region"]
)

co2_metric = Gauge(
    "environment_co2_ppm",
    "CO2 level per region",
    ["region"]
)

temperature_delta_metric = Gauge(
    "environment_temperature_delta",
    "Temperature change since last scrape",
    ["region"]
)

aqi_delta_metric = Gauge(
    "environment_aqi_delta",
    "AQI change since last scrape",
    ["region"]
)

co2_delta_metric = Gauge(
    "environment_co2_delta",
    "CO2 change since last scrape",
    ["region"]
)

def scrape_table():
    response = requests.get(TARGET_URL, timeout=5)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    rows = table.find_all("tr")

    # Read headers
    headers = [th.text.strip() for th in rows[0].find_all("th")]
    col_index = {name: idx for idx, name in enumerate(headers)}

    data = {}

    # Iterate over DATA rows (skip header)
    for row in rows[1:]:
        cols = row.find_all("td")

        # Safety guard
        if len(cols) < len(headers):
            continue

        region = cols[col_index["Region"]].text.strip()
        temperature = float(cols[col_index["Temperature (°C)"]].text.strip())
        aqi = int(cols[col_index["Air Quality Index"]].text.strip())
        co2 = int(cols[col_index["CO₂ (ppm)"]].text.strip())

        data[region] = {
            "temperature": temperature,
            "aqi": aqi,
            "co2": co2
        }

    return data

def main():
    start_http_server(9100)
    print("Exporter running on port 9100")

    global previous_data

    while True:
        current_data = scrape_table()

        for region, values in current_data.items():
            # --- RAW METRICS ---
            temperature_metric.labels(region=region).set(values["temperature"])
            aqi_metric.labels(region=region).set(values["aqi"])
            co2_metric.labels(region=region).set(values["co2"])

            # --- DELTA METRICS ---
            if region in previous_data:
                prev = previous_data[region]

                temperature_delta = values["temperature"] - prev["temperature"]
                aqi_delta = values["aqi"] - prev["aqi"]
                co2_delta = values["co2"] - prev["co2"]
            else:
                # First time we see this region
                temperature_delta = 0
                aqi_delta = 0
                co2_delta = 0

            temperature_delta_metric.labels(region=region).set(temperature_delta)
            aqi_delta_metric.labels(region=region).set(aqi_delta)
            co2_delta_metric.labels(region=region).set(co2_delta)

        # Save current data for next iteration
        previous_data = current_data

        time.sleep(SCRAPE_INTERVAL)


if __name__ == "__main__":
    main()


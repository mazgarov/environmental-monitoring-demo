# Environmental Monitoring Demo
Prometheus · Grafana · Alertmanager · Gotify · Docker Compose

This repository contains a fully working monitoring demo that shows how data from a non-instrumented, legacy-style HTML source can be integrated into a modern observability stack using open-source tools.

The goal of this project is to demonstrate practical integration, not synthetic “hello world” metrics.

---

## Overview

The demo simulates environmental metrics (temperature, air quality index, CO₂ levels) published as a periodically updated HTML table.

These values are:

1. Scraped by a custom Python exporter
2. Collected by Prometheus
3. Visualized in Grafana dashboards
4. Evaluated by alerting rules
5. Sent as notifications via Gotify

All components are deployed using Docker Compose and exposed through a single Nginx entry point.

---

## What This Demo Demonstrates

- Exporting metrics from an HTML table (legacy / external system style)
- Prometheus scraping and rule evaluation
- Grafana dashboards with rankings and delta-based views
- Alerting using both threshold and change-based logic
- Alert notifications delivered to Gotify
- Read-only / demo-friendly access patterns
- Reproducible local and VPS-ready deployment

---

## Architecture
> The following diagram shows the full data flow from a legacy-style HTML source to alert notifications.
```
+------------------+
|  Web Generator   |
|  (HTML table)    |
+--------+---------+
         |
         | HTTP scrape
         v
+------------------+
| Python Exporter  |
| /metrics         |
+--------+---------+
         |
         | Prometheus scrape
         v
+------------------+
|  Prometheus      |
|  Rules & Alerts  |
+--------+---------+
         |
         | Alerts
         v
+------------------+
| Alertmanager     |
+--------+---------+
         |
         | Webhook
         v
+------------------+
| Gotify Adapter   |
+--------+---------+
         |
         v
+------------------+
| Gotify Server    |
| Notifications    |
+------------------+
```
Grafana reads metrics directly from Prometheus.
Nginx exposes all services under a single entry point.

---

## Components

### Web Generator
- Generates synthetic environmental data
- Updates values periodically
- Publishes data as an HTML table

### Exporter
- Scrapes the HTML table
- Converts values into Prometheus metrics
- Handles table structure changes via header-based parsing

### Prometheus
- Scrapes exporter metrics
- Evaluates alert rules
- Stores time-series data

### Grafana
- Visualizes metrics and rankings
- Anonymous, read-only access
- Embedded dashboards for demo use

### Alertmanager
- Groups and routes alerts
- Sends notifications via webhook

### Gotify
- Receives alerts as messages
- Used as an instant notification channel

### Nginx
- Single entry point
- Serves overview and static content
- Proxies internal services
- Designed for future HTTPS support

---

## Demo Access (Local)

Service paths via Nginx:

- Overview: /
- Synthetic Data: /data/
- Grafana: external window
- Prometheus: /prometheus/
- Gotify: /gotify/

---

## Running Locally

Prerequisites:
- Docker
- Docker Compose

Setup:
```
git clone https://github.com/mazgarov/environmental-monitoring-demo.git
cd environmental-monitoring-demo
cp .env.example .env
docker compose up -d --build
```
Note: The demo uses synthetic data and does not require any external credentials.
---

## Alerts & Notifications

Implemented alerts include:
- AQI warning and critical thresholds
- CO₂ sensor failure detection
- Sudden CO₂ spikes (delta-based)

Alerts are grouped and delivered via Gotify.

---

## Security Notes (Demo Scope)

- Grafana is read-only (anonymous viewer)
- Prometheus UI is exposed for educational purposes
- No authentication hardening is applied
- Synthetic data only

---

## Project Structure
```
.
├── docker-compose.yml
├── .env.example
├── nginx/
│   ├── nginx.conf
│   └── html/
│       ├── index.html
│       └── overview/
├── web-generator/
├── exporter/
├── prometheus/
│   ├── prometheus.yml
│   ├── alerts.yml
│   └── rules/
├── grafana/
│   ├── provisioning/
│   └── dashboards/
├── alertmanager/
├── gotify-adapter/
```
---

## Disclaimer

This project uses synthetic data and is intended for demonstration and educational purposes only.
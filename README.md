# Environmental Monitoring — Demo

This repository contains a public demo of an environmental monitoring
and alerting system built with:

- Prometheus
- Grafana
- Alertmanager
- Gotify
- Docker & Docker Compose

All data is **synthetic** and generated in real time.

## Quick start

```bash
cp .env.example .env
docker compose up -d



# Monitoring Demo: Prometheus + Grafana + Alertmanager

This project is a fully working monitoring demo built to show how
existing systems — even those not designed for modern observability —
can be integrated with Prometheus, Grafana, and Alertmanager without
rewriting them.

The demo uses a synthetic data source that simulates environmental
metrics (air quality, CO₂ levels, temperature) and demonstrates
collection, visualization, alerting, and notifications using open-source tools.


## What this demo shows

- Scraping data from a legacy-style HTML table using a custom exporter
- Collecting metrics with Prometheus
- Visualizing time-series and rankings in Grafana
- Triggering alerts based on thresholds and deltas
- Sending notifications to Gotify
- Exposing everything through a single Nginx entry point
- Running the entire stack using Docker Compose


## Architecture
(text + simple ASCII diagram)

## Components
(short explanation of each service)

## Demo access
(local / demo URLs)

## How to run locally
(step-by-step)

## Alerts & notifications
(what alerts exist, where they go)

## Security notes
(read-only, demo limitations)

## Project structure
(tree view)

## Disclaimer
(synthetic data, demo only)

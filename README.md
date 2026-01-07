# 🌍 Environmental Monitoring Demo

**Prometheus · Grafana · Alertmanager · Gotify · Nginx · Docker**

A complete end-to-end **observability demo** that shows how synthetic environmental data can be generated, scraped, visualized, alerted on, and exposed through a secure web interface.

This project is designed as a **technical demo / portfolio project**, not a production monitoring system.

---

## ✨ Motivation

Many real-world systems:

- were built years ago  
- are proprietary or closed  
- were never designed for Prometheus or Grafana  
- cannot be easily rewritten  

This demo demonstrates that:

> **Even legacy or closed systems can be integrated into a modern observability stack without rewriting them.**

By carefully using exporters, adapters, and existing open-source tools, we can extend the life and visibility of existing systems.

---

## 🧱 Architecture Overview

```
┌──────────────────┐
│ Web Generator    │ ← synthetic environment data (HTML table)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Exporter         │ ← scrapes table → exposes Prometheus metrics
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Prometheus       │ ← metrics storage & alert rules
└────────┬─────────┘
         │
         ├──────────────┐
         ▼              ▼
┌──────────────┐ ┌──────────────┐
│ Grafana      │ │ Alertmanager │
│ Dashboards   │ │ Alert logic  │
└──────────────┘ └──────┬───────┘
                        ▼
                 ┌───────────────┐
                 │ Gotify Adapter│
                 └───────┬───────┘
                         ▼
                 ┌───────────────┐
                 │ Gotify Server │
                 │ Notifications │
                 └───────────────┘
```

---

All user access is routed through **Nginx** as a single entry point.

---

## 🧪 Synthetic Data

For each region, the generator produces:

- 🌡 Temperature (°C)
- 🌫 Air Quality Index (AQI)
- 🧪 CO₂ concentration (ppm)

The data intentionally includes:

- gradual changes  
- random spikes  
- sensor failures (CO₂ = 0)  
- recoveries  

This makes dashboards and alerts behave realistically.

---

## 📊 Grafana Dashboards

Dashboards are **provisioned automatically** on startup.

Key panels include:

- AQI trends (all regions)
- Top-5 AQI (current)
- CO₂ sensor failures
- CO₂ sudden deltas
- AQI spike history

Grafana is configured as:

- anonymous access (Viewer)
- read-only
- embeddable
- no alerting (Alertmanager is used instead)

---

## 🚨 Alerting

Alert rules are evaluated in **Prometheus** and routed via **Alertmanager**.

Alert types include:

- AQI warning / critical
- CO₂ sensor failure
- Sudden AQI or CO₂ spikes

Alert noise is reduced using:

- grouping
- repeat intervals
- resolve notifications

---

## 🔔 Notifications (Gotify)

Notifications are delivered using **Gotify**.

Flow:

Alertmanager → Gotify Adapter → Gotify Server

Features:

- severity-based messages
- emoji indicators
- resolved notifications
- demo-friendly configuration

For the public demo, users log in directly to Gotify (Option A).

---

## 🌐 Web Interface

All access is provided through a single Nginx endpoint:

- `/` → Overview page (multilingual)
- `/data/` → Synthetic live data
- Grafana → opened in a new tab
- Prometheus → optional, advanced users
- Gotify → login required

---

## 🔐 Security Notes (Demo Scope)

This project is **not production-hardened by design**.

What *is* done:

- No secrets committed to Git
- Anonymous Grafana is read-only
- Prometheus is optionally exposed
- HTTPS enabled via Let’s Encrypt
- Secrets provided via `.env`

What *is not* done:

- OAuth / SSO
- Fine-grained RBAC everywhere
- Network isolation policies

This balance is intentional for educational clarity.

---

## 🗂 Project Structure
```
.
├── docker-compose.yml
├── .env.example
├── web-generator/
├── exporter/
├── prometheus/
│ ├── prometheus.yml
│ ├── alerts.yml
│ └── prometheus-data/
├── grafana/
│ ├── dashboards/
│ ├── provisioning/
│ └── grafana-data/
├── alertmanager/
│ ├── alertmanager.yml
│ └── alertmanager-data/
├── gotify/
│ └── data/
├── gotify-adapter/
├── nginx/
│ ├── nginx.conf
│ └── html/
│ ├── index.html
│ └── overview/
│ ├── index.html
│ ├── style.css
│ └── lang.js
└── README.md
```

---

## ▶️ Running Locally
```
cp .env.example .env
docker compose up -d --build
```
Open:
http://localhost

---

## 🌍 Deployment Notes

Tested on:

- Ubuntu VPS
- Docker Compose
- Nginx + Let’s Encrypt

Important points:

- Update Grafana root URL for your domain
- Ensure correct volume permissions
- Restart containers after `.env` changes

---

## 🎯 Audience

This project is useful for:

- DevOps engineers
- SRE / monitoring learners
- Architects evaluating observability patterns
- Portfolio and demo purposes

---

## 📌 Final Thought

This demo is not about tools.

It is about **system thinking**:

- minimal invasiveness
- clear separation of concerns
- observability without rewriting systems

---

## Analytics in public demo

The hosted demo uses Umami (privacy-friendly analytics)
to understand interest and usage patterns.

Analytics is enabled **only in the public demo**
and is **not included** in this repository.

---

**Author:**  
Bakhtiyor Mazgarov  
GitHub: https://github.com/mazgarov

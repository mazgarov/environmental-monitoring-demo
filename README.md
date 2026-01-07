# 🌍 Environmental Monitoring Demo
**Prometheus · Grafana · Alertmanager · Gotify · Nginx · Docker**

A complete, self-contained **observability demo** that shows how *synthetic environmental data* can be monitored, visualized, alerted on, and presented via a secure public-facing interface.

This project is designed as a **technical demo / portfolio project**, not a production system.

---

## ✨ Why this project exists

Many real-world systems:
- were built years ago,
- are proprietary or closed,
- were never designed for Prometheus / Grafana,
- cannot be easily rewritten.

This demo shows that:

> **Even legacy or closed systems can be integrated into a modern observability stack without rewriting them.**

By using:
- scraping,
- adapters,
- smart alert grouping,
- and careful exposure,

we can **extend the life and visibility of existing systems**.

---

## 🧱 Architecture Overview


All UI is exposed through a single Nginx entry point


---

## 🧪 What data is simulated?

For each region, the generator produces:

- 🌡 Temperature (°C)
- 🌫 Air Quality Index (AQI)
- 🧪 CO₂ concentration (ppm)

Behavior includes:
- gradual changes,
- random spikes,
- sensor failures (CO₂ = 0),
- recovery events.

This makes dashboards and alerts feel **realistic**, not random.

---

## 📊 Dashboards (Grafana)

The dashboard is provisioned automatically.

- Dashboard UID: `ads5mtp`
- Default URL pattern: `/d/ads5mtp`

Examples:
- Local: http://grafana.localhost/d/ads5mtp
- Production: https://grafana.weather-demo.uz-net.net/d/ads5mtp

Key panels:
- AQI trends (all regions)
- Top-5 AQI right now
- CO₂ sensor failures
- CO₂ sudden deltas
- AQI spike history

Grafana is:
- anonymous (read-only),
- embedded safely,
- alerts disabled (Alertmanager is used instead).

---

## 🚨 Alerting model

Alerts are evaluated in **Prometheus**, routed via **Alertmanager**, and delivered using **Gotify**.

Alert types include:
- AQI warning / critical
- CO₂ sensor failure
- Sudden CO₂ or AQI spikes

### Noise reduction strategy
- Alerts are **grouped**
- Repeats are limited
- Resolve messages are sent
- “Still firing” spam is avoided

---

## 🔔 Notifications (Gotify)

Gotify is used as a **lightweight instant notification system**.

- Alertmanager sends events to a custom adapter
- Adapter formats messages (severity, emoji, values)
- Messages are delivered to Gotify apps / UI

⚠️ This is **Option A**:
- Users log in to Gotify directly
- Viewer users can see messages
- Message deletion is possible (acceptable for demo)

---

## 🌐 Public Web Interface

Everything is accessible from a single entry point:

- `/` → Overview (project explanation, multilingual)
- `/data/` → Synthetic live data
- Grafana → opened in new tab
- Prometheus → optional, advanced users
- Gotify → login required

Nginx is responsible for:
- routing,
- security headers,
- HTTPS termination,
- static content delivery.

---

## 🔐 Security model (Demo-appropriate)

This project is **intentionally not hardened like production**.

What *is* done:
- No exposed databases
- No credentials in Git
- Anonymous Grafana is read-only
- Prometheus UI is optional
- HTTPS enabled
- Secrets via `.env`

What is *not* done:
- RBAC everywhere
- OAuth / SSO
- Network policies

This balance is **intentional for an educational demo**.

---

## 🗂 Project Structure



---

## ▶️ Running locally

```
cp .env.example .env
docker compose up -d --build

Then open:

http://localhost
```

---

## 🌍 Deployment

Tested on:

VPS (Ubuntu)

Docker Compose

Nginx + Let’s Encrypt

Important notes:

Update Grafana root URL for your domain

Ensure correct file permissions on volumes

Restart containers after changing .env

---

## 🎯 Who this is for

DevOps engineers

Monitoring / SRE learners

Architects evaluating observability patterns

Anyone building demos or PoCs

---

## 📌 Final note

This project is not about tools.

It’s about thinking in systems:

separation of concerns,

minimal invasiveness,

observability without rewrite.

---

Author:

Bakhtiyor Mazgarov

GitHub: https://github.com/mazgarov



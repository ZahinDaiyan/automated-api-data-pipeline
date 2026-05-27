# Automated Codeforces Data Pipeline & Dashboard

An asynchronous, fault-tolerant background automation tool that harvests live data from the Codeforces API, manages file logging, and feeds a clean local HTML frontend interface.

## Tech Stack
- **Backend:** Python 3 (Requests, JSON, Time, OS modules)
- **Frontend:** Vanilla HTML5, JavaScript (Async/Fetch API), Water.css
- **Infrastructure:** Python Built-in HTTP Server Architecture

## Features
- Continuous tracking loops running on customized intervals.
- Connection resilience via standard Python exception handling.
- Local decoupled architecture feeding unified data payloads.

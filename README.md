# SentinelFlow: Real-Time Automated Geospatial Emergency Dispatch Engine

SentinelFlow is a high-performance, full-stack automated emergency dispatch management platform designed to optimize field crew logistics. Utilizing a decoupled architecture, the system leverages real-time spatial calculations to automatically match and dispatch the nearest available technician to critical utility hazards (e.g., transformer fires, cable snaps) using live GPS coordinates.

---

## 🚀 Key Features

* **Automated Spatial Dispatch Engine:** Implements localized distance tracking matrices to instantly compute and route the closest available engineer to an incident.
* **High-Fidelity Live Dashboard:** A sleek, dark-mode monitoring control room featuring interactive map layers, custom operational state iconography, and pulsing hazard animations.
* **Real-Time System Metrics:** Interactive telemetry cards updating counts of total workforce assets, active emergencies, and live technician utilization rates on the fly.
* **Containerized Data Infrastructure:** Isolated backend services and relational databases synced seamlessly across dedicated network parameters.

---

## 🛠️ System Architecture & Tech Stack

### Frontend Control Center
* **HTML5 & Tailwind CSS:** Responsive layout framing, terminal log simulation, and administrative configuration consoles.
* **Leaflet.js:** Open-source interactive map rendering utilizing customized HTML vector element markers (`divIcon`) layered over CartoDB smooth dark map tile engines.

### Backend Routing Core
* **FastAPI (Python):** Asynchronous, high-concurrency ASGI web framework handling request validation pipelines.
* **Pydantic:** Strict structural data schema modeling and server-side request payload validation.
* **SQLAlchemy ORM:** Object-Relational Mapping layer abstracting transactional database queries into standard Pythonic declarations.

### Infrastructure & Database
* **Docker & Docker-Compose:** Orchestrator isolating development environments into separate state containers.
* **PostgreSQL:** Relational core system handling state retention for recorded incidents and technician directories.
* **Redis:** High-speed cache manager provisioned to support subsequent message queues.

---

## 📂 Directory Map

```text
sentineflow/
│
├── backend/
│   ├── main.py            # FastAPI Entrypoint & CORS Configuration
│   ├── routes.py          # RESTful Endpoints & Dispatch Optimization Logic
│   ├── models.py          # SQLAlchemy PostgreSQL Database Schema Matrix
│   ├── schemas.py         # Pydantic Structural Data Validators
│   ├── database.py        # Connection String Handlers & Session Closures
│   └── requirements.txt   # Python Dependencies Ecosystem
│
├── frontend/
│   └── index.html         # Leaflet Map Engine & Live Management Dashboard
│
├── docker-compose.yml     # Multi-container Ecosystem Blueprint Configurations
└── .gitignore             # Version Control Pipeline Filters
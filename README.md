Ops Monitor

A lightweight IT operations monitoring dashboard built with Python, FastAPI and Streamlit.

OVERVIEW

Ops Monitor is a small infrastructure monitoring project designed to track system health, website uptime and operational metrics in real time.

The application collects CPU, memory and disk usage metrics, checks website availability, logs historical monitoring data to CSV files and displays active alerts through an interactive dashboard.

FEATURES

- Real-time CPU monitoring
- Real-time memory monitoring
- Real-time disk usage monitoring
- Website uptime monitoring
- Website response time tracking
- Multi-device network monitoring
- Historical CSV logging
- Interactive Streamlit dashboard
- Configurable alert thresholds
- Discord alert notifications
- Discord login notifications
- Environment variable configuration
- Dashboard authentication system
- Docker container support
- FastAPI backend API
- Persistent monitoring history

TECH STACK

Backend

- Python
- FastAPI

Dashboard

- Streamlit
- Plotly

Monitoring

- psutil
- requests

Data Handling

- Pandas
- CSV logging

PROJECT STRUCTURE

ops-monitor/

├── app/
│   ├── alerts.py
│   ├── data_logger.py
│   ├── device_monitor.py
│   ├── discord_alerts.py
│   ├── main.py
│   ├── monitor.py
│   ├── system_stats.py
│   └── website_monitor.py
│
├── config/
│   ├── alert_thresholds.json
│   ├── monitored_devices.json
│   └── monitored_websites.json
│
├── dashboard/
│   └── dashboard.py
│
├── data/
├── logs/
├── .env
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── .gitignore

HOW TO RUN

1. Clone the Repository

git clone https://github.com/LBJevans/ops-monitor.git

cd ops-monitor

2. Create a Virtual Environment

py -m venv venv

3. Activate the Virtual Environment

venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

5. Configure Environment Variables

Create a .env file in the project root:

DISCORD_WEBHOOK_URL=your_discord_webhook
APP_USERNAME=***
APP_PASSWORD=***

RUNNING THE APPLICATION

Start the FastAPI Backend

uvicorn app.main:app --reload

Start the Streamlit Dashboard

Open a second terminal:

streamlit run dashboard/dashboard.py

DOCKER SUPPORT

Run the application using Docker:

docker compose up --build

Dashboard:
http://localhost:8501

API:
http://localhost:8000

API ENDPOINTS

/ -> API health check
/stats -> Returns live system metrics
/websites -> Returns website uptime and response times
/devices -> Returns monitored device status and latency

CURRENT MONITORING CAPABILITIES

System Monitoring

- CPU usage
- Memory usage
- Disk usage

Website Monitoring

- Website uptime status
- HTTP response codes
- Response time measurements

Device Monitoring

- Device/network availability checks
- Latency monitoring
- Multi-device monitoring support

Alerting

- High CPU usage alerts
- High memory usage alerts
- High disk usage alerts
- Offline website alerts
- Offline device alerts
- Discord webhook notifications
- Login notifications

DASHBOARD FEATURES

- Real-time metric updates
- Historical monitoring charts
- Website monitoring table
- Device monitoring table
- Alert display system
- Persistent CSV-backed history
- Login authentication
- Discord-integrated notifications

EXAMPLE TECHNOLOGIES DEMONSTRATED

- REST API development
- Infrastructure monitoring
- Network/device monitoring
- Docker containerisation
- Discord webhook integrations
- Authentication systems
- Environment variable management
- Data logging
- Real-time dashboard development
- Operational alerting systems
- Data visualisation
- Python project architecture

FUTURE IMPROVEMENTS

- SQLite or PostgreSQL database support
- Role-based authentication
- Email notifications
- SSL/HTTPS support
- Advanced analytics dashboards
- Historical uptime percentage reporting
- Cloud deployment
- Kubernetes deployment
- Monitoring agent support
- Centralised logging
- Mobile-friendly dashboard

PROJECT PURPOSE

This project was built as part of a personal portfolio to demonstrate practical skills in:

- IT operations
- Infrastructure monitoring
- Network monitoring
- Backend development
- Dashboard development
- Docker containerisation
- Authentication systems
- Operational analytics
- Alerting systems
- Python application architecture

AUTHOR

Lachlan Evans

GitHub:
https://github.com/LBJevans
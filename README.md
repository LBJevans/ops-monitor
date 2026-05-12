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
- Historical CSV logging
- Interactive Streamlit dashboard
- Active alert system
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
│ ├── alerts.py
│ ├── data_logger.py
│ ├── main.py
│ ├── monitor.py
│ ├── system_stats.py
│ └── website_monitor.py
│
├── dashboard/
│ └── dashboard.py
│
├── data/
├── logs/
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

RUNNING THE APPLICATION

Start the FastAPI Backend

uvicorn app.main:app --reload

Start the Streamlit Dashboard

Open a second terminal:

streamlit run dashboard/dashboard.py

API ENDPOINTS

/ -> API health check
/stats -> Returns live system metrics
/websites -> Returns website uptime and response times

CURRENT MONITORING CAPABILITIES

System Monitoring

- CPU usage
- Memory usage
- Disk usage

Website Monitoring

- Website uptime status
- HTTP response codes
- Response time measurements

Alerting

- High CPU usage alerts
- High memory usage alerts
- High disk usage alerts
- Offline website alerts

DASHBOARD FEATURES

- Real-time metric updates
- Historical monitoring charts
- Website monitoring table
- Alert display system
- Persistent CSV-backed history

EXAMPLE TECHNOLOGIES DEMONSTRATED

- REST API development
- Infrastructure monitoring
- Data logging
- Real-time dashboard development
- Operational alerting systems
- Data visualisation
- Python project architecture

FUTURE IMPROVEMENTS

- SQLite or PostgreSQL database support
- Docker deployment
- Authentication system
- Email or Discord notifications
- Network device monitoring
- Historical uptime analytics
- Configurable monitoring settings
- Background monitoring workers
- Cloud deployment

PROJECT PURPOSE

This project was built as part of a personal portfolio to demonstrate practical skills in:

- IT operations
- Infrastructure monitoring
- Backend development
- Dashboard development
- Operational analytics
- Alerting systems
- Python application architecture

AUTHOR

Lachlan Evans

GitHub:
https://github.com/LBJevans
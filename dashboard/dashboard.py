import os
import sys
import time
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.alerts import (
    generate_system_alerts,
    generate_website_alerts,
    generate_device_alerts
)

from app.discord_alerts import (
    send_discord_alert,
    send_login_notification
)

from dotenv import load_dotenv

load_dotenv()

APP_USERNAME = os.getenv("APP_USERNAME")
APP_PASSWORD = os.getenv("APP_PASSWORD")

STATS_API_URL = "http://127.0.0.1:8000/stats"
WEBSITE_API_URL = "http://127.0.0.1:8000/websites"
DEVICE_API_URL = "http://127.0.0.1:8000/devices"

SYSTEM_LOG_FILE = "data/system_metrics.csv"
WEBSITE_LOG_FILE = "data/website_metrics.csv"

st.set_page_config(
    page_title="Ops Monitor Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #f5f5f5;
    }

    .stMetric {
        background-color: #161b22;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #30363d;
    }

    .stDataFrame {
        border-radius: 12px;
    }

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔐 Ops Monitor Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == APP_USERNAME and password == APP_PASSWORD:
            st.session_state.authenticated = True
            send_login_notification(username)
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()

with st.sidebar:
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

st.title("🖥️ Ops Monitor")
st.caption("Real-time infrastructure monitoring, uptime checks and operational alerts.")

def fetch_stats():
    try:
        response = requests.get(STATS_API_URL, timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None

def fetch_websites():
    try:
        response = requests.get(WEBSITE_API_URL, timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return []

def load_system_history():
    if os.path.exists(SYSTEM_LOG_FILE):
        return pd.read_csv(SYSTEM_LOG_FILE)
    return pd.DataFrame()

def fetch_devices():
    try:
        response = requests.get(DEVICE_API_URL, timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return []

def load_website_history():
    if os.path.exists(WEBSITE_LOG_FILE):
        return pd.read_csv(WEBSITE_LOG_FILE)
    return pd.DataFrame()

stats = fetch_stats()
website_data = fetch_websites()
device_data = fetch_devices()

if stats is None:
    st.error("API is not running. Start the FastAPI server first.")
    st.code("uvicorn app.main:app --reload", language="powershell")
    st.stop()

system_df = load_system_history()
website_df = load_website_history()

latest = stats

system_alerts = generate_system_alerts(stats)
website_alerts = generate_website_alerts(website_data)
device_alerts = generate_device_alerts(device_data)

all_alerts = system_alerts + website_alerts + device_alerts

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{latest['cpu_percent']}%")

with col2:
    st.metric("Memory Usage", f"{latest['memory_percent']}%")

with col3:
    st.metric("Disk Usage", f"{latest['disk_percent']}%")

st.subheader("Active Alerts")

if all_alerts:
    for alert in all_alerts:
        st.error(alert)
        send_discord_alert(alert)
else:
    st.success("✅ No active alerts")

st.divider()

st.subheader("System Usage History")

if not system_df.empty:
    cpu_chart = px.line(
        system_df,
        x="timestamp",
        y="cpu_percent",
        title="CPU Usage Over Time"
    )
    st.plotly_chart(cpu_chart, use_container_width=True)

    memory_chart = px.line(
        system_df,
        x="timestamp",
        y="memory_percent",
        title="Memory Usage Over Time"
    )
    st.plotly_chart(memory_chart, use_container_width=True)

    disk_chart = px.line(
        system_df,
        x="timestamp",
        y="disk_percent",
        title="Disk Usage Over Time"
    )
    st.plotly_chart(disk_chart, use_container_width=True)
else:
    st.warning("No system history available yet.")

st.divider()

st.subheader("Website Monitoring")

if website_data:
    current_website_df = pd.DataFrame(website_data)

    st.dataframe(
        current_website_df,
        use_container_width=True
    )
else:
    st.warning("No website monitoring data available.")

st.divider()

st.subheader("Website Uptime Summary")

if not website_df.empty:
    uptime_summary = (
        website_df.groupby("website")["status"]
        .apply(lambda x: round((x == "ONLINE").mean() * 100, 2))
        .reset_index(name="uptime_percent")
    )

    st.dataframe(
        uptime_summary,
        use_container_width=True
    )
else:
    st.warning("No uptime data available yet.")

st.divider()

st.subheader("Device Monitoring")

if device_data:
    device_df = pd.DataFrame(device_data)

    st.dataframe(
        device_df,
        use_container_width=True
    )
else:
    st.warning("No device monitoring data available.")

st.subheader("Website Response Time History")

if not website_df.empty:
    response_chart = px.line(
        website_df,
        x="timestamp",
        y="response_time_ms",
        color="website",
        title="Website Response Time Over Time"
    )
    st.plotly_chart(response_chart, use_container_width=True)

    st.dataframe(
        website_df.tail(50),
        use_container_width=True
    )
else:
    st.warning("No website history available yet.")

time.sleep(5)
st.rerun()
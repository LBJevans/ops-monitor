import time
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

API_URL = "http://127.0.0.1:8000/stats"

st.set_page_config(
    page_title="Ops Monitor Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Ops Monitor Dashboard")
st.caption("Lightweight IT operations and infrastructure monitoring dashboard.")

def fetch_stats():
    try:
        response = requests.get(API_URL, timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None

if "history" not in st.session_state:
    st.session_state.history = []

stats = fetch_stats()

if stats is None:
    st.error("API is not running. Start the FastAPI server first.")
    st.code("cd app\nuvicorn main:app --reload", language="powershell")
    st.stop()

st.session_state.history.append(stats)

df = pd.DataFrame(st.session_state.history)

latest = df.iloc[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{latest['cpu_percent']}%")

with col2:
    st.metric("Memory Usage", f"{latest['memory_percent']}%")

with col3:
    st.metric("Disk Usage", f"{latest['disk_percent']}%")

st.divider()

st.subheader("System Usage Over Time")

cpu_chart = px.line(
    df,
    x="timestamp",
    y="cpu_percent",
    title="CPU Usage Over Time"
)
st.plotly_chart(cpu_chart, use_container_width=True)

memory_chart = px.line(
    df,
    x="timestamp",
    y="memory_percent",
    title="Memory Usage Over Time"
)
st.plotly_chart(memory_chart, use_container_width=True)

disk_chart = px.line(
    df,
    x="timestamp",
    y="disk_percent",
    title="Disk Usage Over Time"
)
st.plotly_chart(disk_chart, use_container_width=True)

st.divider()

st.subheader("Raw Monitoring Data")
st.dataframe(df, use_container_width=True)

time.sleep(5)
st.rerun()
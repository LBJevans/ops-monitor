import json
import os

CONFIG_FILE = "config/alert_thresholds.json"

DEFAULT_THRESHOLDS = {
    "cpu_threshold": 80,
    "memory_threshold": 80,
    "disk_threshold": 90
}

def load_thresholds():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_THRESHOLDS

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def generate_system_alerts(stats):
    alerts = []
    thresholds = load_thresholds()

    if stats["cpu_percent"] > thresholds["cpu_threshold"]:
        alerts.append(f"⚠️ High CPU Usage: {stats['cpu_percent']}%")

    if stats["memory_percent"] > thresholds["memory_threshold"]:
        alerts.append(f"⚠️ High Memory Usage: {stats['memory_percent']}%")

    if stats["disk_percent"] > thresholds["disk_threshold"]:
        alerts.append(f"⚠️ High Disk Usage: {stats['disk_percent']}%")

    return alerts

def generate_website_alerts(websites):
    alerts = []

    for website in websites:
        if website["status"] == "OFFLINE":
            alerts.append(f"🚨 Website Offline: {website['website']}")

    return alerts
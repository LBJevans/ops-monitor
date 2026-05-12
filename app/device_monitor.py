import json
import os
from datetime import datetime

from ping3 import ping

CONFIG_FILE = "config/monitored_devices.json"

def load_devices():
    if not os.path.exists(CONFIG_FILE):
        return []

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config.get("devices", [])

def check_devices():
    results = []

    devices = load_devices()

    for device in devices:
        try:
            response = ping(device["host"], timeout=2)

            if response is not None:
                results.append({
                    "device": device["name"],
                    "host": device["host"],
                    "status": "ONLINE",
                    "latency_ms": round(response * 1000, 2),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            else:
                results.append({
                    "device": device["name"],
                    "host": device["host"],
                    "status": "OFFLINE",
                    "latency_ms": None,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

        except Exception:
            results.append({
                "device": device["name"],
                "host": device["host"],
                "status": "OFFLINE",
                "latency_ms": None,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    return results
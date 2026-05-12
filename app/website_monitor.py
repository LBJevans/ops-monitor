import json
import os
from datetime import datetime

import requests

CONFIG_FILE = "config/monitored_websites.json"

def load_websites():
    if not os.path.exists(CONFIG_FILE):
        return []

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config.get("websites", [])

def check_websites():
    results = []

    websites = load_websites()

    for website in websites:
        try:
            response = requests.get(website, timeout=5)

            results.append({
                "website": website,
                "status": "ONLINE",
                "status_code": response.status_code,
                "response_time_ms": round(response.elapsed.total_seconds() * 1000, 2),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        except requests.exceptions.RequestException:
            results.append({
                "website": website,
                "status": "OFFLINE",
                "status_code": None,
                "response_time_ms": None,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    return results
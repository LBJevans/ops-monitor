import requests
from datetime import datetime

WEBSITES = [
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com"
]

def check_websites():
    results = []

    for website in WEBSITES:
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
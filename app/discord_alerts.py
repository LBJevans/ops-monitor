import os

import requests
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_alert(message):
    if not DISCORD_WEBHOOK_URL:
        return

    payload = {
        "content": message
    }

    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
    except requests.exceptions.RequestException:
        pass

def send_login_notification(username):
    if not DISCORD_WEBHOOK_URL:
        return

    payload = {
        "content": f"🔐 User login detected: {username}"
    }

    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
    except requests.exceptions.RequestException:
        pass
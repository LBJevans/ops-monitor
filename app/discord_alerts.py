import os
import requests
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_alert(message: str) -> None:
    if not DISCORD_WEBHOOK_URL:
        return

    payload = {"content": message}

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        pass

def send_login_notification(username: str) -> None:
    if not DISCORD_WEBHOOK_URL:
        return

    payload = {"content": f"🔐 User login detected: {username}"}

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        pass
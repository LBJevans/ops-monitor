import csv
import os
from datetime import datetime


DATA_DIR = "data"
SYSTEM_LOG_FILE = os.path.join(DATA_DIR, "system_metrics.csv")
WEBSITE_LOG_FILE = os.path.join(DATA_DIR, "website_metrics.csv")
DEVICE_LOG_FILE = os.path.join(DATA_DIR, "device_metrics.csv")


def ensure_data_directory():
    os.makedirs(DATA_DIR, exist_ok=True)


def log_system_metrics(stats):
    ensure_data_directory()

    file_exists = os.path.isfile(SYSTEM_LOG_FILE)

    with open(SYSTEM_LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp",
                "cpu_percent",
                "memory_percent",
                "disk_percent"
            ]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(stats)


def log_website_metrics(results):
    ensure_data_directory()

    file_exists = os.path.isfile(WEBSITE_LOG_FILE)

    with open(WEBSITE_LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp",
                "website",
                "status",
                "status_code",
                "response_time_ms"
            ]
        )

        if not file_exists:
            writer.writeheader()

        for result in results:
            writer.writerow({
                "timestamp": result.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                "website": result.get("website"),
                "status": result.get("status"),
                "status_code": result.get("status_code"),
                "response_time_ms": result.get("response_time_ms")
            })


def log_device_metrics(results):
    ensure_data_directory()

    file_exists = os.path.isfile(DEVICE_LOG_FILE)

    with open(DEVICE_LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp",
                "device",
                "host",
                "status",
                "latency_ms"
            ]
        )

        if not file_exists:
            writer.writeheader()

        for result in results:
            writer.writerow({
                "timestamp": result.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                "device": result.get("device"),
                "host": result.get("host"),
                "status": result.get("status"),
                "latency_ms": result.get("latency_ms")
            })
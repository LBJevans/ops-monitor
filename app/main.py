from fastapi import FastAPI

from app.data_logger import log_system_metrics, log_website_metrics, log_device_metrics
from app.device_monitor import check_devices
from app.system_stats import get_system_stats
from app.website_monitor import check_websites

app = FastAPI(title="Ops Monitor API")

@app.get("/")
def root():
    return {"message": "Ops Monitor API Running"}

@app.get("/stats")
def stats():
    system_stats = get_system_stats()
    log_system_metrics(system_stats)
    return system_stats

@app.get("/websites")
def websites():
    website_results = check_websites()
    log_website_metrics(website_results)
    return website_results

@app.get("/devices")
def devices():
    device_results = check_devices()
    log_device_metrics(device_results)
    return device_results
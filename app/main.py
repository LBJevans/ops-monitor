from fastapi import FastAPI
from app.system_stats import get_system_stats
from app.website_monitor import check_websites

app = FastAPI(title="Ops Monitor API")

@app.get("/")
def root():
    return {"message": "Ops Monitor API Running"}

@app.get("/stats")
def stats():
    return get_system_stats()

@app.get("/websites")
def websites():
    return check_websites()
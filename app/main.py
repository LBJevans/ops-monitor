from fastapi import FastAPI
from system_stats import get_system_stats

app = FastAPI(title="Ops Monitor API")

@app.get("/")
def root():
    return {"message": "Ops Monitor API Running"}

@app.get("/stats")
def stats():
    return get_system_stats()
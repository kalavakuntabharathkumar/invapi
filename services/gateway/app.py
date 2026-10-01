import os
import httpx
from fastapi import FastAPI, HTTPException
app=FastAPI(title="API Gateway",version="0.1.0")
@app.get("/health")
def health(): return {"service":"gateway","status":"ok"}
@app.get("/services")
def services():
    return {"orders":os.getenv("ORDER_URL","http://localhost:8001"),
            "inventory":os.getenv("INVENTORY_URL","http://localhost:8002"),
            "customers":os.getenv("CUSTOMER_URL","http://localhost:8003")}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app=FastAPI(title="Inventory Service",version="0.1.0")
stock={"SKU-001":100,"SKU-002":45,"SKU-003":0}
class Reservation(BaseModel):
    sku:str
    quantity:int=Field(gt=0,le=1000)
@app.get("/health")
def health(): return {"service":"inventory","status":"ok"}
@app.get("/inventory/{sku}")
def get_stock(sku:str):
    if sku not in stock: raise HTTPException(404,"SKU not found")
    return {"sku":sku,"available":stock[sku]}
@app.post("/inventory/reservations")
def reserve(body:Reservation):
    available=stock.get(body.sku)
    if available is None: raise HTTPException(404,"SKU not found")
    if available<body.quantity: raise HTTPException(409,"Insufficient stock")
    stock[body.sku]-=body.quantity
    return {"sku":body.sku,"reserved":body.quantity,"remaining":stock[body.sku]}

# Inventory reservation rejects requests that exceed available stock.

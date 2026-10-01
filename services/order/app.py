import json, os, uuid
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app = FastAPI(title="Order Service", version="0.1.0")
orders = {}
class OrderIn(BaseModel):
    customer_id: str
    sku: str
    quantity: int = Field(gt=0, le=1000)
class OrderOut(OrderIn):
    id: str
    status: str
    created_at: str
@app.get("/health")
def health(): return {"service":"order","status":"ok"}
@app.post("/orders", response_model=OrderOut, status_code=201)
def create_order(payload: OrderIn):
    item = {"id":str(uuid.uuid4()), **payload.model_dump(), "status":"PENDING",
            "created_at":datetime.now(timezone.utc).isoformat()}
    orders[item["id"]] = item
    # Publish an event when Kafka is configured; order creation remains available without it.
    try:
        from confluent_kafka import Producer
        broker = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        if broker:
            producer = Producer({"bootstrap.servers":broker})
            producer.produce("order.created", key=item["id"], value=json.dumps(item))
            producer.flush(2)
    except Exception:
        # In production, use an outbox/retry strategy rather than silently losing events.
        pass
    return item
@app.get("/orders")
def list_orders(): return list(orders.values())
@app.get("/orders/{order_id}", response_model=OrderOut)
def get_order(order_id:str):
    if order_id not in orders: raise HTTPException(404,"Order not found")
    return orders[order_id]

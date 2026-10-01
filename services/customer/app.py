from fastapi import FastAPI, HTTPException
app=FastAPI(title="Customer Service",version="0.1.0")
customers={"C-100":{"id":"C-100","name":"Sample Customer","tier":"standard"}}
@app.get("/health")
def health(): return {"service":"customer","status":"ok"}
@app.get("/customers/{customer_id}")
def get_customer(customer_id:str):
    if customer_id not in customers: raise HTTPException(404,"Customer not found")
    return customers[customer_id]

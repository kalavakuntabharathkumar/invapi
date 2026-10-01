# Order & Inventory Microservices Platform (starter implementation)

A runnable educational scaffold showing service separation, PostgreSQL persistence, Docker Compose, and Kafka event contracts.

## Services
- `order-service` — create and retrieve orders; publishes `order.created` when Kafka is configured.
- `inventory-service` — stock lookup and reservation endpoint.
- `customer-service` — basic customer profile endpoint.
- `api-gateway` — small routing entry point / health endpoint.

## Run locally
```bash
docker compose up --build
```
API docs:
- Order service: http://localhost:8001/docs
- Inventory service: http://localhost:8002/docs
- Customer service: http://localhost:8003/docs
- Gateway: http://localhost:8000/docs

This repository is a generated starter project, not a verified reproduction of an existing production system. Performance, failure-rate, user-count, and deployment metrics in a resume must be independently measured before being claimed.

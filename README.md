# IRCTC Booking Toolkit - Microservices Monorepo

This repository provides a scaffolded microservices architecture for an IRCTC booking automation toolkit. Each service is an independent FastAPI app with minimal stub endpoints to wire the overall flow.

## Services

- auth-service: login and session refresh
- train-search-service: search trains and seat availability
- booking-service: booking preferences (quota/coach/class)
- passenger-service: manage passengers and attach to booking
- captcha-service: manual captcha relay
- payment-service: payment initiate and status
- orchestrator-service: end-to-end workflow coordinator
- notification-service: email/SMS notifications

## Quick start (Docker Compose)

Prerequisites: Docker + Docker Compose

```bash
docker compose build
docker compose up
```

Services will listen on:
- 8001 auth-service
- 8002 train-search-service
- 8003 booking-service
- 8004 passenger-service
- 8005 captcha-service
- 8006 payment-service
- 8007 orchestrator-service
- 8008 notification-service

## Local run (without Docker)

Prerequisites: Python 3.11+ (recommended 3.12)

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
uvicorn --app-dir services/auth-service/app main:app --port 8001
```

Repeat for other services by switching the `--app-dir` and `--port`.

## Endpoints (stubs)

- auth-service
  - POST /login
  - GET /refresh-session
  - GET /health
- train-search-service
  - GET /trains?from=HYB&to=NDLS&date=2025-08-30&class=SL
  - GET /train/{trainNumber}/seats?class=SL
  - GET /health
- booking-service
  - POST /booking/preference
  - GET /health
- passenger-service
  - POST /passenger
  - GET /passengers
  - POST /booking/passengers
  - GET /health
- captcha-service
  - GET /captcha
  - POST /captcha
  - GET /health
- payment-service
  - POST /payment/initiate
  - GET /payment/status/{id}
  - GET /health
- orchestrator-service
  - POST /booking/start
  - GET /booking/status
  - GET /health
- notification-service
  - POST /notify/email
  - POST /notify/sms
  - GET /health

## Orchestrator wiring

The orchestrator uses the following env vars (provided in docker-compose):
- AUTH_URL, TRAIN_SEARCH_URL, BOOKING_URL, PASSENGER_URL, CAPTCHA_URL, PAYMENT_URL, NOTIFICATION_URL

## Notes

- All endpoints are placeholders suitable for wiring and local testing. Integrating with real IRCTC APIs requires compliance with their terms, handling captcha, sessions, and payment gateway redirections securely.
- Add persistence/backing stores (e.g., PostgreSQL) and secrets management before production use.

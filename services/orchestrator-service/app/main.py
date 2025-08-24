from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os

app = FastAPI(title="orchestrator-service")

class BookingStartRequest(BaseModel):
	from_station: str
	to_station: str
	date: str
	class_code: str
	quota: str

class BookingStatus(BaseModel):
	status: str
	step: str | None = None

@app.post("/booking/start", response_model=BookingStatus)
async def start_booking(req: BookingStartRequest):
	# Placeholder orchestration: sanity-call dependent services' health endpoints
	urls = [
		os.getenv("AUTH_URL"),
		os.getenv("TRAIN_SEARCH_URL"),
		os.getenv("BOOKING_URL"),
		os.getenv("PASSENGER_URL"),
		os.getenv("CAPTCHA_URL"),
		os.getenv("PAYMENT_URL"),
	]
	async with httpx.AsyncClient(timeout=5.0) as client:
		for base in urls:
			if not base:
				continue
			await client.get(f"{base}/health")
	return BookingStatus(status="STARTED", step="initialized")

@app.get("/booking/status", response_model=BookingStatus)
def get_status():
	return BookingStatus(status="IN_PROGRESS", step="waiting_for_captcha")

@app.get("/health")
def health():
	return {"service": os.getenv("SERVICE_NAME", "orchestrator-service"), "status": "ok"}
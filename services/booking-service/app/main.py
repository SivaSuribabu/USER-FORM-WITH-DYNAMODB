from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="booking-service")

class BookingPreference(BaseModel):
	quota: str  # General, Tatkal, PremiumTatkal
	coach: str | None = None
	class_code: str

@app.post("/booking/preference")
def set_preference(pref: BookingPreference):
	return {"message": "Preference set", "data": pref.model_dump()}

@app.get("/health")
def health():
	return {"service": os.getenv("SERVICE_NAME", "booking-service"), "status": "ok"}
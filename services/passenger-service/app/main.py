from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os

app = FastAPI(title="passenger-service")

class Passenger(BaseModel):
	name: str
	age: int
	gender: str
	berth_preference: str | None = None

_passengers: List[Passenger] = []

@app.post("/passenger")
def add_passenger(p: Passenger):
	_passengers.append(p)
	return {"message": "Passenger added"}

@app.get("/passengers", response_model=List[Passenger])
def get_passengers():
	return _passengers

@app.post("/booking/passengers")
def attach_passengers(passengers: List[Passenger]):
	if not passengers:
		raise HTTPException(status_code=400, detail="No passengers provided")
	return {"message": "Passengers attached", "count": len(passengers)}

@app.get("/health")
def health():
	return {"service": os.getenv("SERVICE_NAME", "passenger-service"), "status": "ok"}
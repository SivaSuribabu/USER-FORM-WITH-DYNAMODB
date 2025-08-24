from fastapi import FastAPI, Query
from pydantic import BaseModel
import os

app = FastAPI(title="train-search-service")

class Train(BaseModel):
	number: str
	name: str
	from_station: str
	to_station: str
	class_code: str
	date: str

class SeatAvailability(BaseModel):
	train_number: str
	class_code: str
	availability: str

@app.get("/trains")
def search_trains(from_: str = Query(alias="from"), to: str = Query(...), date: str = Query(...), class_: str = Query(alias="class")):
	return [
		Train(number="12723", name="TELANGANA EXP", from_station=from_, to_station=to, class_code=class_, date=date),
	]

@app.get("/train/{trainNumber}/seats", response_model=SeatAvailability)
def seats(trainNumber: str, class_: str = Query(alias="class")):
	return SeatAvailability(train_number=trainNumber, class_code=class_, availability="AVAILABLE 12")

@app.get("/health")
def health():
	return {"service": os.getenv("SERVICE_NAME", "train-search-service"), "status": "ok"}
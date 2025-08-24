from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import os

app = FastAPI(title="notification-service")

class EmailRequest(BaseModel):
	to: EmailStr
	subject: str
	body: str

class SmsRequest(BaseModel):
	phone: str
	message: str

@app.post("/notify/email")
def notify_email(req: EmailRequest):
	return {"message": "Email queued", "to": req.to}

@app.post("/notify/sms")
def notify_sms(req: SmsRequest):
	return {"message": "SMS queued", "to": req.phone}

@app.get("/health")
def health():
	return {"service": os.getenv("SERVICE_NAME", "notification-service"), "status": "ok"}
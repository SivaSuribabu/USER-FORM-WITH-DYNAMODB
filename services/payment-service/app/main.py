from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="payment-service")

class PaymentInitiate(BaseModel):
	amount: float
	method: str  # UPI, NetBanking, Card, Wallet

@app.post("/payment/initiate")
def initiate_payment(body: PaymentInitiate):
	return {"payment_id": "pay_123", "status": "PENDING", "amount": body.amount, "method": body.method}

@app.get("/payment/status/{payment_id}")
def payment_status(payment_id: str):
	return {"payment_id": payment_id, "status": "SUCCESS"}

@app.get("/health")
def health():
	return {"service": os.getenv("SERVICE_NAME", "payment-service"), "status": "ok"}
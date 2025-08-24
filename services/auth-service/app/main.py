from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import os

app = FastAPI(title="auth-service")

class LoginRequest(BaseModel):
	username: str
	password: str
	captcha: str | None = None

class LoginResponse(BaseModel):
	session_token: str
	message: str

class RefreshResponse(BaseModel):
	session_token: str

@app.post("/login", response_model=LoginResponse)
def login(body: LoginRequest):
	# Placeholder: authenticate with IRCTC (manual captcha handling via captcha-service)
	if not body.username or not body.password:
		raise HTTPException(status_code=400, detail="Missing credentials")
	return LoginResponse(session_token="dummy-session-token", message="Logged in")

@app.get("/refresh-session", response_model=RefreshResponse)
def refresh_session():
	return RefreshResponse(session_token="dummy-session-token-refreshed")

@app.get("/health")
def health():
	return {"service": os.getenv("SERVICE_NAME", "auth-service"), "status": "ok"}
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="captcha-service")

class CaptchaSubmit(BaseModel):
	captcha: str

@app.get("/captcha")
def get_captcha():
	# In reality this would proxy an image; placeholder returns a token
	return {"captcha_id": "dummy-captcha-id", "image_url": "/static/captcha.png"}

@app.post("/captcha")
def post_captcha(body: CaptchaSubmit):
	return {"message": "Captcha received", "captcha": body.captcha}

@app.get("/health")
def health():
	return {"service": os.getenv("SERVICE_NAME", "captcha-service"), "status": "ok"}
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY services/booking-service/app/ /app/
EXPOSE 8003
ENV PORT=8003
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
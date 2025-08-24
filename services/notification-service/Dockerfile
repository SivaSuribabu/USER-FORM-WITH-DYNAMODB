FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY services/notification-service/app/ /app/
EXPOSE 8008
ENV PORT=8008
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8008"]
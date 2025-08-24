FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY services/passenger-service/app/ /app/
EXPOSE 8004
ENV PORT=8004
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004"]
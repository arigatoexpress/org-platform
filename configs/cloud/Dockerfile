FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    ORG_PLATFORM_OFFLINE=false

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir .

CMD ["python", "scripts/run_intel_demo.py"]

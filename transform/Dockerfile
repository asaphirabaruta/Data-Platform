FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY transform_load.py .

ENTRYPOINT ["python", "transform_load.py"]

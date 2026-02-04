FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY people.csv .
RUN pip install --no-cache-dir -r requirements.txt

COPY ingest.py .

CMD ["python", "app.py"]  # all logs go to stdout

ENTRYPOINT ["python", "ingest.py"]

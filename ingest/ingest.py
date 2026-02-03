import pandas as pd
from datetime import date
from minio import Minio

client = Minio(
    "minio:9000",
    access_key="minio",
    secret_key="minio123",
    secure=False,
)

bucket = "raw"
if not client.bucket_exists(bucket):
    client.make_bucket(bucket)

df = pd.read_csv("people.csv")

today = date.today()
path = f"source_a/{today.year}/{today.month}/{today.day}/data.csv"

df.to_csv("/tmp/data.csv", index=False)
client.fput_object(bucket, path, "/tmp/data.csv")

print(f"Uploaded raw data to {path}")

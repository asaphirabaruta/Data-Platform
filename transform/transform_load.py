from xmlrpc import client
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from minio import Minio

# Postgres connection (docker-compose service)
DB_URL = "postgresql://platform:platform@postgres:5432/warehouse"

def calculate_age(dob_str):
    try:
        dob = pd.to_datetime(dob_str, errors="coerce")
        if pd.isna(dob):
            return None
        today = datetime.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    except Exception:
        return None

def main():
    
    # Minio client setup (docker-compose service)
    client = Minio(
        "minio:9000",
        access_key="minio",
        secret_key="minio123",
        secure=False,
    )

    # Load raw data from Minio raw file 
    client.fget_object("raw", "source_a/2026/2/3/data.csv", "/tmp/raw.csv")
    df = pd.read_csv("/tmp/raw.csv")

    # ---- Data Cleaning ----
    # Drop rows with missing User Id
    df = df.dropna(subset=["User Id"])
    
    # Remove duplicates by User Id
    df = df.drop_duplicates(subset=["User Id"])

    # Standardize Sex column
    df["Sex"] = df["Sex"].str.upper().map({"MALE":"M", "FEMALE":"F"}).fillna("U")

    # Derive Age
    df["Age"] = df["Date of birth"].apply(calculate_age)

    # Optional: derive Full Name
    df["Full Name"] = df["First Name"].str.strip() + " " + df["Last Name"].str.strip()

    # Select relevant columns for warehouse
    warehouse_cols = ["User Id", "Full Name", "Sex", "Email", "Phone", "Age", "Job Title"]
    df_warehouse = df[warehouse_cols]

    # ---- Load to Postgres ----
    engine = create_engine(DB_URL)
    df_warehouse.to_sql("users", engine, if_exists="replace", index=False)

    print(f"Loaded {len(df_warehouse)} rows into Postgres table 'users'")

if __name__ == "__main__":
    main()

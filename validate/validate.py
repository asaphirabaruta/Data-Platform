import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://platform:platform@postgres:5432/warehouse"

def main():
    engine = create_engine(DB_URL)

    # Load table from Postgres
    df = pd.read_sql("SELECT * FROM users", engine)

    errors = []

    # ---- 1. Null Checks ----
    null_cols = ["User Id", "Email"]
    for col in null_cols:
        null_count = df[col].isna().sum()
        if null_count > 0:
            errors.append(f"Column '{col}' has {null_count} NULL values")

    # ---- 2. Duplicate Checks ----
    dup_count = df.duplicated(subset=["User Id"]).sum()
    if dup_count > 0:
        errors.append(f"Found {dup_count} duplicate User Ids")

    # ---- 3. Row Count Check ----
    if df.shape[0] == 0:
        errors.append("No rows found in users table!")

    if errors:
        for e in errors:
            print(f"[ERROR] {e}")
        raise Exception("Data validation failed!")
    else:
        print(f"[OK] Data validation passed! {df.shape[0]} rows.")

if __name__ == "__main__":
    main()

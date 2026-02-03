FROM python:3.11-slim

WORKDIR /dbt

# Install dbt with Postgres adapter
RUN pip install --no-cache-dir dbt-postgres

COPY dbt_project.yml .
COPY profiles.yml .
COPY models ./models

ENTRYPOINT ["dbt"]

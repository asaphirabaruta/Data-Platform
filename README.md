# Data & ML Platform – Containerized Reference Stack

## Overview

This repository contains a **containerized data and ML-ready platform** designed to demonstrate:
- Data ingestion and storage
- Transformation and analytics modeling
- Data quality validation
- ML readiness
- Centralized logging and observability

The entire stack runs locally using **Docker Compose**, enabling reproducibility without external cloud dependencies.

The project emphasizes **engineering clarity, observability, and extensibility**, rather than tool over-complexity.

---

## Architecture

    +------------------+
    |   CSV Dataset    |
    +--------+---------+
             |
             v
    +------------------+
    | Ingestion (Py)   |
    | - Fetch CSV     |
    | - Store raw     |
    +--------+---------+
             |
             v
    +------------------+
    | MinIO (S3 API)   |
    | raw/source/date |
    +--------+---------+
             |
             v
    +------------------+
    | Transform & Load |
    | - Clean data    |
    | - Normalize     |
    +--------+---------+
             |
             v
    +------------------+
    | PostgreSQL       |
    | Data Warehouse  |
    +--------+---------+
             |
             v
    +------------------+
    | dbt              |
    | - staging models |
    | - marts          |
    | - tests          |
    +------------------+


---

## Tech Stack

| Layer | Technology |
|-----|-----------|
| Ingestion | Python |
| Object Storage | MinIO (S3 compatible) |
| Warehouse | PostgreSQL |
| Transformations | Python |
| Analytics Modeling | dbt |
| Data Validation | dbt tests + Python |
| Observability | Loki, Promtail, Grafana |
| Orchestration | Docker Compose |

---

## Services

### Core Services

| Service | Description |
|------|------------|
| `postgres` | Data warehouse |
| `minio` | Raw data storage |
| `ingest` | Downloads and stores raw CSV data |
| `transform` | Cleans and loads data into Postgres |
| `validate` | Data quality validation |
| `dbt` | Analytics models and tests |

### Observability

| Service | Description |
|-------|------------|
| `loki` | Log aggregation backend |
| `promtail` | Collects container logs |
| `grafana` | Log exploration and dashboards |

---

## Dataset

The ingested dataset contains user-related information with fields such as:

- User Id
- First Name
- Last Name
- Sex
- Email
- Phone
- Date of Birth
- Job Title

After transformation, the data is loaded into a normalized warehouse table.

---

## How to Run

### Prerequisites

- Docker
- Docker Compose

### Start the Stack

```bash
docker compose up -d --build

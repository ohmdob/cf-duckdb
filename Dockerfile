FROM python:3.10-slim AS build

# Set destination for COPY
WORKDIR /app

COPY container_src/server.py ./
COPY container_src/barcode_th.parquet ./

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python", "server.py"]


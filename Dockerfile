# Dockerfile
FROM python:3.13-slim

WORKDIR /app

# Copy requirements early to leverage Docker caching
COPY requirements.txt .

# Install netcat and Python dependencies
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Copy project files into the image
COPY . .

# Make the entrypoint executable and use it
ENTRYPOINT ["/app/entrypoint.sh"]

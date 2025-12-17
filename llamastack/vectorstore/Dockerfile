FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the setup script
COPY setup-vectorstore.py .

# Make script executable
RUN chmod +x setup-vectorstore.py

# Run the setup script
ENTRYPOINT ["python3", "setup-vectorstore.py"]


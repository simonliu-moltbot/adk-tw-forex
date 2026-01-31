# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set PYTHONPATH
ENV PYTHONPATH=/app

# Expose the port
EXPOSE 8000

# Run the ADK Web UI
# Pointing to /app where 'tw_forex' directory (the agent) resides
CMD ["adk", "web", "/app", "--port", "8000", "--host", "0.0.0.0"]

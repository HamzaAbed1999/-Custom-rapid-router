# Use Python 3.8 slim as the base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -e .


# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "example_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]

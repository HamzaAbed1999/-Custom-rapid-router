# Use an official Python runtime as a parent image
FROM python:3.11-slim

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
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY example_project/ /app/example_project/
COPY game/ /app/game/

# Collect static files
RUN python /app/example_project/manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Define the default command to run the application
CMD ["gunicorn", "example_project.wsgi:application", "--bind", "0.0.0.0:8000"]
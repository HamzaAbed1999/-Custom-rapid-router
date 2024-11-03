# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Accept build argument
ARG BASE_URL

# Set environment variable from build argument
ENV BASE_URL=${BASE_URL}

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python3 example_project/manage.py collectstatic --noinput
RUN python3 example_project/manage.py migrate --noinput
# Expose port 8000
EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "example_project.wsgi:application", "--bind", "0.0.0.0:8000"]

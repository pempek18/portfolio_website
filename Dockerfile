# Use Python base image with specific version
FROM python:3.9.18-slim-bullseye

# Add metadata labels
LABEL maintainer="pempek183@gmail.com"
LABEL description="This is a personal portfolio website built with Flask and deployed on Docker."
LABEL version="1.0"

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Install system dependencies including wkhtmltopdf and its dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wkhtmltopdf \
    xvfb \
    xfonts-75dpi \
    xfonts-base \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create necessary directories including /static/img
RUN mkdir -p static/img
RUN mkdir -p templates

# Copy static files FIRST (before other files)
COPY static/img/ static/img/

# Create and switch to non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy requirements and install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app.py ./
COPY templates/ ./templates/
COPY static/ ./static/

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 5000

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Command to run the application
CMD ["python", "app.py"] 
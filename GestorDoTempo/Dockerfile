# Pull official base image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose port
EXPOSE 8000

# Run entrypoint script (optional, but good for waiting for DB)
# ENTRYPOINT ["/app/entrypoint.sh"]

# Default command
CMD ["gunicorn", "GestorDoTempo.wsgi:application", "--bind", "0.0.0.0:8000"]

# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies, including portaudio for PyAudio
RUN apt-get update && apt-get install -y

# Ensure pip is up-to-date
RUN python -m ensurepip --upgrade
RUN python -m pip install --upgrade pip

# Copy requirements.txt and verify it exists
COPY requirements.txt .
RUN ls -l requirements.txt || echo "requirements.txt not found!"

# Copy the FastAPI app code
COPY main.py .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
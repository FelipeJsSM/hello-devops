# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables for Flask and disable buffering for gunicorn
ENV PYTHONUNBUFFERED=1

# Use gunicorn to serve the application in production
# The application factory pattern requires specifying app:create_app()
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]

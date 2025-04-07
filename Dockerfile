# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Flask
RUN pip install Flask

# Copy app code into container
COPY app.py .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

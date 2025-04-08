FROM python:3.11-slim
ARG VERSION

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code into container
COPY app.py .

ENV VERSION=${VERSION}

EXPOSE 5001

CMD ["python", "app.py"]

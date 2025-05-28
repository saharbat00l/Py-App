# Use official Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose port your app will run on (adjust if needed)
EXPOSE 5000

# Command to run the app (adjust if your main app file or start command differs)
CMD ["python", "app.py"]

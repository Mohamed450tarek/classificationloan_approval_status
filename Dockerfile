# Use official Python image (stable)
FROM python:3.11


# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install build tools + dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "app_joblib:app", "--host", "0.0.0.0", "--port", "8000" ]

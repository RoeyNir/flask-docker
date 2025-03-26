FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the working directory
COPY app.py .
COPY requirements.txt .

# Install dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 (used by the Flask app)
EXPOSE 5000

# Define the default command to run the application
CMD ["python", "app.py"]
# Start with a clean Python 3.13 image
FROM python:3.13-slim

# Set the folder inside the container where our code lives
WORKDIR /app

# Copy the requirements file and install the libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your actual script
COPY add_numbers.py .

# Open port 80 so the internet can talk to the app
EXPOSE 80

# The command to start the web server
CMD ["uvicorn", "add_numbers:app", "--host", "0.0.0.0", "--port", "80"]

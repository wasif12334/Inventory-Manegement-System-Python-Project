# Use an official Py
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Run app.py when the container launches
CMD ["python", "main.py"]
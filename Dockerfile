# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the working directory
COPY . .
# Download the ZIP file
# Install gdown to download files from Google Drive
RUN pip install gdown

# Download the ZIP file from Google Drive
RUN gdown --id 1Ld8E7yuDyQU2dTTGtTHcIflJ5ft16I4x -O wiki.vi.model.zip
# Extract the Word2Vec model from the ZIP file
RUN unzip wiki.vi.model.zip -d data

# Expose the port on which the Flask application will run (optional)
EXPOSE 5000

# Set the environment variable for Flask (optional)
ENV FLASK_APP=main.py

# Run the Flask application when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]

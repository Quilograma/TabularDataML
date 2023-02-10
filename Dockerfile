# Use the official Python 3.8 image as the base image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Make the shell script executable
RUN chmod +x run.sh

# Define the command to run when the container starts
CMD [ "./run.sh" ]



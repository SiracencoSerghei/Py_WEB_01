
# Use the official Python image as the base image
FROM python:3.11-slim

# Install build-essential for compilation
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy both pyproject.toml and poetry.lock to the working directory
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-interaction --no-ansi

# Copy the entire project to the working directory
COPY . /app/

# Set up a directory for user data
RUN mkdir /app/user_data

# Set the working directory for user data
WORKDIR /app/user_data

# Specify the command to run on container start
CMD ["poetry", "run", "Py_WEB_01/Py_WEB_01/__main__.py"]



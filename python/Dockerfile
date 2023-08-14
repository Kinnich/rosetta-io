# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

ENV DOCKER_HOST="ssh://coffee"

FROM r-base:4.3.1

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

# Install the jsonlite package
RUN R -e "install.packages('jsonlite')"
RUN R -e "install.packages('base64enc')"

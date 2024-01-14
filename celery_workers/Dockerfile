# Use an Alpine-based Python image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Install build dependencies (needed for some Python packages)
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    cargo

# Install Poetry
RUN pip install poetry

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Remove build dependencies to keep the image small
RUN apk del .build-deps

# Run the application
CMD ["poetry", "run", "start_workers"]


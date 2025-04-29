FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential curl

# Install Rust and Cargo
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    echo 'export PATH="/root/.cargo/bin:$PATH"' >> /root/.bashrc && \
    . "$HOME/.cargo/env" && \
    rustup --version && \
    cargo --version

# Add Cargo's bin directory to the PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Run the main.py script inside the container when it starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

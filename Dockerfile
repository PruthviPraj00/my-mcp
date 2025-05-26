FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip

# Copy only the requirements first for better caching
COPY pyproject.toml .

# Copy the rest of the application
COPY . .

# Install dependencies directly (no venv in Docker)
RUN pip install -e .

# Expose the port that the server will run on
EXPOSE 8000

# Run the MCP server
CMD ["python", "main.py"]

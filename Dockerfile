FROM python:3.11-slim

WORKDIR /app

# Install uv for faster dependency installation
RUN pip install uv

# Copy the rest of the application
COPY . .

# Install dependencies using uv
RUN uv pip install -e .

CMD ["uv", "run", "main.py"]

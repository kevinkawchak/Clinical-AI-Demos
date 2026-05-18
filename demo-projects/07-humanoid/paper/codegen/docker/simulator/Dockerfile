FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir numpy pandas pyarrow duckdb scipy
COPY src/ ./src/
CMD ["python", "src/iterate.py"]

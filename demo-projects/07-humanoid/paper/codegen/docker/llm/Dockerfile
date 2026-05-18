FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir numpy pandas pyarrow duckdb jsonschema pyyaml scipy anthropic cryptography
COPY src/ ./src/
ENV PYTHONPATH=/app/src
CMD ["python", "-m", "site_runtime"]

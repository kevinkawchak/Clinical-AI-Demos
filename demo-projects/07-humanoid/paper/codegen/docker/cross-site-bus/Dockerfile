FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir jsonschema cryptography
COPY src/cross_site_bus.py ./
ENV PHI_EGRESS=forbidden
CMD ["python", "cross_site_bus.py"]

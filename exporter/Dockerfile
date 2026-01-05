FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    requests \
    beautifulsoup4 \
    prometheus_client

COPY exporter.py .

EXPOSE 9100

CMD ["python", "exporter.py"]


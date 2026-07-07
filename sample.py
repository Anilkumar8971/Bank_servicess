FROM python:3.9-slim

WORKDIR /app

COPY sample.py .

CMD ["python", "sample.py"]

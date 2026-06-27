FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY analyze_dump.py .
COPY xt22_dump.txt .

CMD ["python", "analyze_dump.py"]
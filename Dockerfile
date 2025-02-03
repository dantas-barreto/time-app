FROM python:3.10

WORKDIR /app

COPY time.py .

CMD ["python", "time.py"]

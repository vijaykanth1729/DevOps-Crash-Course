FROM python:3.11-slim

WORKDIR /app

RUN python -m pip install --no-cache-dir flask

COPY python_app.py /app/python_app.py

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "python_app.py"]

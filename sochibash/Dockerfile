FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "sochibash.wsgi:application", "--bind", "0:8000" ]
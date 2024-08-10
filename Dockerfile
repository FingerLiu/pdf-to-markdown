FROM python:3.12.5-bookworm

RUN apt-get update

COPY requirements.txt /tmp/

RUN pip install -U pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

ADD . /app

WORKDIR /app
CMD ["uvicorn", "app.main:app",  "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app/backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
FROM python:3.11

# environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV app_port 8000

COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt
FROM python:3.8

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install psycopg2 psycopg2-binary gunicorn gevent
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x db.sh

ENTRYPOINT ["bash","./db.sh"]

CMD ["gunicorn","fsit.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "120", "-k", "gevent", "--workers" ,"4"]
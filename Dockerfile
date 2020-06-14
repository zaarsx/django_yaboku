FROM python:3.8

ENV PYTHONBUFFERED 1

RUN pip install uwsgi==2.0.18

COPY ./uwsgi.ini /uwsgi.ini

WORKDIR /srv
ADD ./src/ /srv

RUN pip install -r requirements.txt


RUN python manage.py collectstatic


CMD uwsgi --ini /uwsgi.ini --gid=1000 --uid=1000

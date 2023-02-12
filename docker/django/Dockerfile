FROM python:3.11-slim as builder
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev python3-dev

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
RUN apt-get purge -y gcc python3-dev && apt-get autoremove -y

FROM builder as prod
RUN pip install gunicorn gevent
COPY ./docker/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /app
COPY . .
ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "gunicorn", "main.wsgi:application", "-c=gunicorn.conf.py"]
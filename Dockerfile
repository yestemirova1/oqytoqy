FROM python:3.8.3-alpine3.11

ENV PYTHONUNBUFFERED=1 COLUMNS=200 TZ=Asia/Almaty

ADD ./src/requirements.txt ./src/dev_requirements.txt

RUN sed -i "s/dl-cdn.alpinelinux.org/mirror.neolabs.kz/g" /etc/apk/repositories \
    && apk update \
    && apk --no-cache add bash postgresql-dev binutils gdal-dev geos-dev gettext \
    && apk --no-cache add --virtual .build-deps tzdata libffi-dev gcc g++ curl-dev libressl-dev musl-dev make \
    && ln -fs /usr/share/zoneinfo/Asia/Almaty /etc/localtime \
    && echo "Asia/Almaty" > /etc/timezone \
    && pip install --upgrade pip \
    && pip install --no-cache-dir celery==5.0.5 cent==3.0.1 Django==3.1.7 django-cors-headers==3.7.0 django-environ==0.4.5 django-extensions==3.1.1 django-filter==2.4.0 django-fsm==2.7.1 djangorestframework==3.12.2 future==0.18.2 gunicorn==20.0.4 gevent==21.1.2 ipython==7.20.0 packaging==20.9 psycopg2-binary==2.8.6 pyjwt==2.0.1 requests==2.25.1 sentry-sdk==0.20.3 whitenoise==5.2.0 \
    && apk del .build-deps

COPY ./src /src

WORKDIR /src
CMD ["./entrypoint.sh"]

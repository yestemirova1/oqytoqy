FROM python:3.8.3-alpine3.11

ENV PYTHONUNBUFFERED=1 COLUMNS=200 \
    TZ=Asia/Almaty PIP_CONFIG_FILE=/src/pip.conf

ADD ./src/requirements.txt \
    ./src/dev_requirements.txt

RUN sed -i "s/dl-cdn.alpinelinux.org/mirror.neolabs.kz/g" /etc/apk/repositories \
    && apk update \
    && apk --no-cache add bash postgresql-dev binutils gdal-dev geos-dev gettext \
    && apk --no-cache add --virtual .build-deps tzdata libffi-dev gcc g++ curl-dev libressl-dev musl-dev make \
    && ln -fs /usr/share/zoneinfo/Asia/Almaty /etc/localtime \
    && echo "Asia/Almaty" > /etc/timezone \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -Ur /src/requirements.txt \
    && apk del .build-deps

COPY ./src /src

WORKDIR /src
CMD ["./entrypoint.sh"]

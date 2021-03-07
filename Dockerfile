FROM python:3.8-alpine3.11

ENV PYTHONUNBUFFERED=1 COLUMNS=200 \
    TZ=Asia/Almaty PIP_CONFIG_FILE=/src/pip.conf

ADD ./src/requirements.txt \
    ./src/dev_requirements.txt \
    ./src/pip.conf /src/

RUN sed -i "s/dl-cdn.alpinelinux.org/mirror.neolabs.kz/g" \
    /etc/apk/repositories \
    && apk update \
    && apk --no-cache add bash postgresql-dev binutils gdal-dev geos-dev \
# Django translations
    gettext \
# Add build dependencies
    && apk --no-cache add --virtual .build-deps \
    tzdata libffi-dev gcc g++ curl-dev libressl-dev \
    musl-dev make \
# Set timezone
    && ln -fs /usr/share/zoneinfo/Asia/Almaty /etc/localtime \
    && echo "Asia/Almaty" > /etc/timezone \
# Upgrade pip
    && pip install --upgrade pip \
# Add project dependencies
    && pip install --no-cache-dir -Ur /src/requirements.txt \
    --no-cache-dir -Ur /src/dev_requirements.txt \
# Remove build dependencies
    && apk del .build-deps

COPY ./src /src

WORKDIR /src
CMD ["/src/entrypoint.sh"]

FROM python:3.8.3-alpine3.11

ENV PYTHONUNBUFFERED=1 COLUMNS=200 \
    TZ=Asia/Almaty PIP_CONFIG_FILE=/src/pip.conf

ADD ./src/requirements.txt \
    ./src/dev_requirements.txt \
    ./src/pip.conf /src/

RUN sed -i "s/dl-cdn.alpinelinux.org/mirror.neolabs.kz/g" /etc/apk/repositories

COPY ./src /src

WORKDIR /src
CMD ["./entrypoint.sh"]

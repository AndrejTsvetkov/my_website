FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc jpeg-dev zlib-dev libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk add libjpeg
RUN apk del .tmp

RUN mkdir /app
COPY . /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
COPY ./media /vol/web/media

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol

RUN chown user:user /app
RUN chown -R user:user db.sqlite3
RUN chmod -R 755 db.sqlite3
USER user

CMD ["entrypoint.sh"]
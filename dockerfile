## Build
FROM python:bullseye AS build

WORKDIR /app

# Download dependencies
COPY ./photo.jpg ./
COPY ./main.py ./
COPY ./session.session ./

RUN pip install telethon
RUN pip install pause

CMD ["python"]

## Deploy
FROM gcr.io/distroless/base-debian11

WORKDIR /

COPY --from=build /app/telegram_spammer /telegram_spammer

EXPOSE 80/tcp

USER root:root

ENTRYPOINT ["/telegram_spammer"]

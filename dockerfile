## Build
FROM python:bullseye AS build

WORKDIR /app

# Download dependencies
COPY ./photo.jpg ./
COPY ./main.py ./
COPY ./session.session ./

RUN pip install telethon
RUN pip install pause
RUN ls
RUN ls ../

CMD ["python"]

## Deploy
FROM gcr.io/distroless/base-debian11

WORKDIR /

COPY --from=build /app/ /

EXPOSE 80/tcp

USER root:root

ENTRYPOINT ["/"]

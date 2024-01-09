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

## Deploy
FROM gcr.io/distroless/base-debian11

ENTRYPOINT ["python"]
CMD ["main.py"]

USER root:root
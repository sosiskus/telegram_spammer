## Build
FROM python:3.12

WORKDIR /app

# Download dependencies
COPY ./photo.jpg ./
COPY ./main.py ./
COPY ./session.session ./

RUN pip install telethon pause
RUN ls
RUN ls ../

## Deploy
FROM gcr.io/distroless/base-debian11

ENTRYPOINT ["python3"]
CMD ["main.py"]

USER root:root
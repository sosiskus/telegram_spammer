## Build
FROM python:3.12

WORKDIR /app

# Download dependencies
COPY ./photo.jpg ./
COPY ./main.py ./
COPY ./session.session ./

RUN pip install telethon pause
RUN ls
RUN python --version

ENTRYPOINT ["python3", "main.py"]
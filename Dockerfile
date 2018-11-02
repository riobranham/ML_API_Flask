FROM python:3.6-slim

LABEL maintainer="rio.branham@gmail.com"

USER root

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

ENV NAME World

CMD ["python", "model.py"]

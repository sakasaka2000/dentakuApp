FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN /bin/sh -c pip install -r requirements.txt
COPY . /code

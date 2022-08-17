FROM python:3.9-alpine

ENV PYTHONBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv venv 
RUN source venv/bin/activate
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app

 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /djdocker
 WORKDIR /djdocker
 ADD requirements.txt /djdocker/
 RUN pip install -r requirements.txt
 ADD . /djdocker/

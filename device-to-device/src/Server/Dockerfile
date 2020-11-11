FROM ubuntu:18.04
RUN apt-get update

RUN apt-get install -y -q build-essential python-pip python-dev python-simplejson git
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv

ADD . /deployment/
RUN virtualenv /deployment/env/
RUN /deployment/env/bin/pip install flask
WORKDIR /deployment
CMD env/bin/python app.py
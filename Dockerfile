FROM ubuntu:14.04

MAINTAINER ryanolee<rizza@rizza.net>

#Build python 3.6 and add py qt bindings
RUN sudo apt-get update -y && \
    sudo apt-get install python3 python3-pyqt4 python3-pip xvfb -y

WORKDIR /app/

COPY . /app/

RUN pip3 install -r requirements.txt

VOLUME ['/app/chaps']
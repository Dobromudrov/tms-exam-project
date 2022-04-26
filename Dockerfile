# FROM python:3.9.5
#
#
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt
#
#
# WORKDIR /rentcar
# COPY . /webexam/


FROM python:3.9.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/rentcar

COPY requirements.txt ./

RUN pip3 install -r requirements.txt
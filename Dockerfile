FROM python:3.9

RUN pip install --upgrade pip \
    && pip install pyppeteer

WORKDIR /src

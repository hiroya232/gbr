FROM python:3.9-buster

COPY requirements.txt /src/

RUN pip install --upgrade pip \
    && pip install -r /src/requirements.txt

RUN apt-get update \
    && apt-get install -y gconf-service libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxss1 libxtst6 libappindicator1 libnss3 libasound2 libatk1.0-0 libc6 ca-certificates fonts-liberation lsb-release xdg-utils wget

RUN apt-get install -y zsh vim zsh-autosuggestions zsh-syntax-highlighting \
    && chsh -s /bin/zsh

RUN apt-get install -y gettext libcurl4-gnutls-dev libexpat1-dev libghc-zlib-dev libssl-dev make less \
    && wget https://github.com/git/git/archive/v2.35.1.tar.gz \
    && tar -xzf v2.35.1.tar.gz \
    && cd git-* \
    && make prefix=/usr/local all \
    && make prefix=/usr/local install \
    && rm -rf git-2.35.1*

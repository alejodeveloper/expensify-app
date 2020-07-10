FROM python:latest

RUN apt-get update && apt-get install -y gcc ssh openssh-server gettext postgresql-client libpq-dev \
    libjpeg-dev libopenjp2-7-dev wget zsh

RUN mkdir /app/

WORKDIR /app

COPY ./expensify/ /app/
COPY ./docker-entrypoint.sh /app/
RUN pip install -r requirements/base-pip-requirements.txt

RUN mkdir /var/run/sshd

# INSTALL OHMYZSH INTO THE CONTAINER
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

RUN echo "cd /app/expensify-app" >> /root/.zshrc

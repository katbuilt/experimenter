FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1

RUN groupadd --gid 10001 app && \
    useradd --uid 10001 --gid 10001 --home /app --create-home app

WORKDIR /app

EXPOSE 7001

# Wait for the db to initialize
COPY bin/wait-for-it.sh /app/bin/wait-for-it.sh
RUN chmod +x /app/bin/wait-for-it.sh

RUN apt-get update
RUN apt-get install -y postgresql-client 

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir --disable-pip-version-check

COPY . /app

USER app

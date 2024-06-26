FROM python:3.11-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user


ENV PATH="/py/bin:$PATH"


USER django-user
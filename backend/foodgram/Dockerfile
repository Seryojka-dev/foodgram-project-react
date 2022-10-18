#FROM python:3.7-slim

#RUN apt update && apt -y install libpq-dev build-essential

#WORKDIR /app

#COPY requirements.txt /app

#RUN apt update && apt -y install libpq-dev build-essential

#RUN pip install --upgrade pip && pip3 install -r requirements.txt --no-cache-dir

#COPY ../ /app

#CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]

FROM python:3.7-slim
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app
RUN apt-get update && apt-get -y install libpq-dev build-essential
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./ /app
CMD ["gunicorn", "foodgram_api.wsgi:application", "--bind", "0:8000" ]

FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /frog/frog
COPY requirements.txt /frog/frog/
RUN pip install -r requirements.txt
COPY . /frog/frog/
FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD ./src/requirements.txt /src/
RUN pip install -r requirements.txt
ADD ./src/ /src/

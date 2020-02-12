FROM python:3.7-alpine
MAINTAINER Grant Steinfeld "grant.steinfeld@ibm.com"
RUN apk add gcc g++ make libffi-dev openssl-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY ./src /app/src
ENTRYPOINT ["python"]
CMD [ "src/main.py" ]

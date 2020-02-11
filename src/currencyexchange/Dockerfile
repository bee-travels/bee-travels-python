FROM python:3.7-alpine
MAINTAINER Grant Steinfeld "grant.steinfeld@ibm.com"
RUN apk add gcc g++ make libffi-dev openssl-dev
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD python3 src/main.py

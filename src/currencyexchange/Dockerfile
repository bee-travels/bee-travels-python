FROM registry.access.redhat.com/ubi8/ubi
MAINTAINER Grant Steinfeld grant.steinfeld@ibm.com
RUN yum install -y python3; yum clean all
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
COPY ./src /app/src
ENTRYPOINT ["python3"]
CMD ["src/main.py"]

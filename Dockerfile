FROM ubuntu:artful

WORKDIR /app

ADD . /app

RUN apt-get update -y
RUN apt-get install curl -y
RUN apt-get install python3 -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip install awscli
RUN pip install boto3

COPY s3_policy_report.py /s3_policy_report.py

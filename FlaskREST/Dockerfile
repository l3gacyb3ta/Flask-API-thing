FROM registry.access.redhat.com/ubi8/ubi

RUN dnf install -y python38 python3-pip

RUN mkdir api

COPY ./* /api

WORKDIR /api

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]

EXPOSE 5000
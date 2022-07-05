FROM python:3.8-slim-buster

WORKDIR /app/alexnetcc

RUN pip install torch

ADD . / ./

RUN pip install -r requirements.txt

EXPOSE 5007

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]
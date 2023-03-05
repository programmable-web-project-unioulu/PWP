FROM python:3.8.10-slim-buster

ENV DOCKER True

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /db

RUN python3 populate.py

CMD ["python3", "api.py"]

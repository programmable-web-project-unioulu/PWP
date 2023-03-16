FROM python:3.8.10-slim-buster

ENV DOCKER True
ENV FLASK_APP dogdict

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /src/app/

COPY . .

<<<<<<< HEAD
WORKDIR /
=======
RUN ls
>>>>>>> 34d5235 (Huge commit to refactor resources, tests and api, models, utils in different packages)

# Creates initial test db
RUN flask init-db

<<<<<<< HEAD
CMD ["flask", "run"]
=======
CMD ["flask", "run", "--host=0.0.0.0"]
>>>>>>> 34d5235 (Huge commit to refactor resources, tests and api, models, utils in different packages)

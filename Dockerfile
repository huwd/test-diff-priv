FROM python:3.9.4-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY test.py test.py
COPY PUMS.csv PUMS.csv
COPY PUMS.yaml PUMS.yaml

CMD [ "python3", "test.py"]

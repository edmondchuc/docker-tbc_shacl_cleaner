FROM python:3.8-alpine

WORKDIR /home

ADD app.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD python3 app.py input/${SHACL_FILE}
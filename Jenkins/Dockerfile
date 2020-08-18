FROM python:3.7-slim-stretch

COPY requirements.txt /opt/requirements.txt
COPY app.py /opt/app.py

RUN apt-get update && apt-get -y install gcc python3-dev

RUN pip install -r /opt/requirements.txt

EXPOSE 5000

CMD ["python", "/opt/app.py"]

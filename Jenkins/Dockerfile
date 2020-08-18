FROM python:3.7-slim-stretch

COPY requirements.txt /opt/requirements.txt
COPY web_example.py /opt/app.py

RUN pip install -r /opt/requirements.txt

EXPOSE 5000

CMD ["python", "/opt/app.py"]

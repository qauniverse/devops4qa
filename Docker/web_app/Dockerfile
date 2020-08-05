FROM python:3.7-slim-stretch

COPY requirements.txt /opt/requirements.txt
COPY web_example.py /opt/web_example.py

RUN pip install -r /opt/requirements.txt

EXPOSE 5000

CMD ["python", "/opt/web_example.py"]

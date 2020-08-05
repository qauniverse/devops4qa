FROM debian:stable-slim

RUN apt update && apt install python3 -y

COPY example.py /opt/example.py

RUN chmod +x /opt/example.py

CMD ["/opt/example.py"]

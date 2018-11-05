FROM python:3

RUN apt-get update && apt-get install -y cython && apt-get clean

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR app
COPY server.py server.py

CMD ["gunicorn", "-b", "0.0.0.0:5000", "server:app"]

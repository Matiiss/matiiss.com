FROM python:3.10-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--access-logfile", "-", "-w", "4", "-b", "0.0.0.0:8000", "main.py:app"]

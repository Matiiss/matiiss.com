FROM python:3.11-slim-bookworm

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "flask_app", "run", "--port", "5000"]

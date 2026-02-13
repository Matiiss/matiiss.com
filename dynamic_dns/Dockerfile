FROM python:3.10-slim

ARG UID=1000
ARG GID=1000
ARG USERNAME=user

RUN apt-get update && apt-get install -y --no-install-recommends sudo

RUN groupadd -g ${GID} ${USERNAME} \
    && useradd -u ${UID} -g ${GID} -m ${USERNAME} \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ${USERNAME}

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
RUN sudo apt-get install -y --no-install-recommends miniupnpc

COPY requirements.txt requirements.txt
RUN uv venv --python 3.10 \
    && uv pip install -r requirements.txt

COPY main.py main.py

RUN sudo chown -R ${UID}:${GID} .

CMD ["uv", "run", "python", "/app/main.py"]

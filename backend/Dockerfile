FROM python:3.10-slim AS base

ARG UID=1000
ARG GID=1000
ARG USERNAME=user

RUN apt-get update && apt-get install -y --no-install-recommends sudo

RUN groupadd -g ${GID} ${USERNAME} && useradd -u ${UID} -g ${GID} -m ${USERNAME} && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ${USERNAME}

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN sudo mkdir /app && sudo chown ${UID}:${GID} /app
WORKDIR /app

EXPOSE 8000


FROM base AS dev

RUN sudo apt-get install -y --no-install-recommends git


FROM base AS prod

COPY requirements.txt requirements.txt
RUN uv venv --python="3.10" && uv pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "--access-logfile", "-", "-w", "4", "-b", "0.0.0.0:8000", "flask_app:app"]

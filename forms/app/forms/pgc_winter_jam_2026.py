from pathlib import Path

import httpx
from flask import Blueprint, abort, jsonify, render_template, request

NAME = Path(__file__).stem
TITLE = ""
DESCRIPTION = ""

app = Blueprint(name=NAME, import_name=__name__, url_prefix=f"/{NAME}")


@app.get("/")
def index():
    return render_template("base.html", title=TITLE, description=DESCRIPTION, form_name=NAME)


@app.post("/submit")
def submit():
    abort(405)


@app.post("/validate_username")
def validate_username():
    if not request.is_json:
        abort(415)

    data = request.json
    username = data["username"]

    is_valid, message = _validate_username(username=username)

    return jsonify({"is_valid": is_valid, "message": message})


def _validate_username(username: str) -> tuple[bool, str]:
    response = httpx.get(f"https://itch.io/profile/{username.lower()}")
    if response.status_code == 404:
        return False, "Username does not exist on itch.io"

    return True, ""


def get_blueprint() -> Blueprint:
    return app

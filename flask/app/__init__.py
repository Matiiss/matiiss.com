from flask import Flask, render_template
from flask_assets import Environment
from webassets.bundle import Bundle

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle("sass/style.scss", filters="pyscss", output="css/style.css")
assets.register("style", scss)


@app.route("/")
def index():
    return render_template("index.html", title="Matiiss")


if __name__ == "__main__":
    app.run(port=8080, debug=True)

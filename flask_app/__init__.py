from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)

# let nginx cache the static files
app.config.update(SEND_FILE_MAX_AGE_DEFAULT=0)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle("sass/style.scss", filters="pyscss", output="css/style.css")
assets.register("style", scss)


@app.route("/")
def index():
    return render_template("index.html", title="Matiiss")

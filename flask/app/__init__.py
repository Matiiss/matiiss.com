from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle("sass/style.scss", filters="pyscss", output="css/style.css")
assets.register("style", scss)

skillset = {
    "Languages": ["Python", "C", "C++", "JavaScript", "HTML", "CSS", "Lua", "Bash"],
    "Technologies": [
        "Git",
        "SSH",
        "GitHub",
        "DigitalOcean",
        "Docker",
        "Nginx",
        "Apache",
        "Ansible",
        "Django",
        "Flask",
        "Pygame",
        "Bootstrap",
        "Python C API",
        "acme.sh",
    ],
}


@app.route("/")
def index():
    return render_template("index.html", title="Matiiss", skillset=skillset)


if __name__ == "__main__":
    app.run(port=8080, debug=True)

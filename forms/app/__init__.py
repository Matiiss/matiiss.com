import importlib
from pathlib import Path

from flask import Flask

app = Flask(__name__)

module_names = [
    p.stem for p in (Path(__file__).parent / "forms").iterdir() if not p.name.startswith("_") and p.name.endswith(".py")
]

for name in module_names:
    module = importlib.import_module(f".forms.{name}", package=__package__)
    app.register_blueprint(module.get_blueprint())


def main():
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()

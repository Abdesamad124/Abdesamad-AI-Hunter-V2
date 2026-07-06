from flask import Flask, render_template, request
import os

from core.engine import AIHunterEngine

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

engine = AIHunterEngine()


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        file = request.files["image"]

        if file:

            path = os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )

            file.save(path)

            result = engine.analyze(path)

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
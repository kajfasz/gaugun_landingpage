from flask import Flask, render_template

from content import LINKS, SITE

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", site=SITE, links=LINKS)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

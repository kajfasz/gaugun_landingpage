from flask import Flask, abort, render_template

from content import COPY, LINKS, SITE

ALLOWED_ICONS = frozenset({"facebook", "instagram", "youtube", "mail"})
ALLOWED_LANGS = frozenset(COPY)

app = Flask(__name__)


@app.after_request
def _secure_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    response.headers["Content-Security-Policy"] = (
        "default-src 'none'; img-src 'self'; style-src 'self'; "
        "frame-ancestors 'none'; base-uri 'none'; form-action 'none'"
    )
    return response


def _links(copy):
    contact = {
        "title": copy["contact_title"],
        "url": f"mailto:{SITE['email']}",
        "note": SITE["email"],
        "icon": "mail",
    }
    links = []
    for link in (*LINKS, contact):
        if link["icon"] not in ALLOWED_ICONS:
            raise RuntimeError(f"unknown icon: {link['icon']}")
        links.append(link)
    return links


def _page(lang):
    if lang not in ALLOWED_LANGS:
        abort(404)
    copy = COPY[lang]
    if copy["other_lang"] not in ALLOWED_LANGS:
        abort(404)
    return render_template(
        "index.html",
        site=SITE,
        copy=copy,
        links=_links(copy),
    )


@app.route("/")
def index_pl():
    return _page("pl")


@app.route("/en")
def index_en():
    return _page("en")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

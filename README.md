# GauGun

Prosty landing zespołu: logo, opis, linki, naklejki i QR.

## Uruchomienie lokalne

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Strona wstaje na [http://127.0.0.1:5000](http://127.0.0.1:5000). Angielska wersja: `/en`.

`python app.py` trzyma debuger tylko na localhost. Na serwerze używaj gunicorn, bez `debug=True`:

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## Treść

Wszystko siedzi w `content.py`:

- `SITE` — nazwa, rok, adres strony i mail
- `COPY` — teksty PL/EN
- `LINKS` — Facebook, Instagram, YouTube

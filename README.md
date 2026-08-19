# GauGun

Prosty landing zespołu: logo, krótki opis i linki.

## Uruchomienie

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Strona wstaje na [http://127.0.0.1:5000](http://127.0.0.1:5000).

Na serwerze (nasłuch na wszystkich interfejsach):

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## Treść

Wszystko siedzi w `content.py`:

- `SITE` — nazwa i krótki opis
- `LINKS` — lista odnośników

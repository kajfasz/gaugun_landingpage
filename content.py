from urllib.parse import urlparse

from markupsafe import Markup

SITE = {
    "name": "Gaugun",
    "year": 2026,
    "url": "https://gaugun.duckdns.org/",
    "email": "gaugunband@gmail.com",
}
SITE["host"] = urlparse(SITE["url"]).netloc

COPY = {
    "pl": {
        "html_lang": "pl",
        "other_lang": "en",
        "other_path": "/en",
        "switch_label": "English",
        "description": (
            "Czterech typów grających rocka tak, jakby ostatnie 30 lat w muzyce "
            "wydarzyło się przez przypadek."
        ),
        "bio": [
            Markup(
                "<strong>Gaugun</strong> to czterech typów grających rocka tak, "
                "jakby ostatnie 30 lat w muzyce wydarzyło się przez przypadek. "
                "Trochę klasycznego rocka, trochę punkowego brudu, ciężkie riffy "
                "i zdecydowanie za dużo wzmacniaczy. Inspiracje? AC/DC, Black Sabbath, "
                "Pidżama Porno i wszystko, przy czym można jednocześnie kiwać głową "
                "i rozlać piwo."
            ),
            (
                "Gramy głośno, po swojemu i bez zbędnego kombinowania. Jeśli lubisz "
                "brudne gitary, prosty przekaz i koncerty, po których lekko piszczy "
                "w uszach — prawdopodobnie się dogadamy."
            ),
        ],
        "links_heading": "Linki",
        "contact_title": "Kontakt",
        "qr_alt": "Kod QR do strony Gaugun",
        "qr_caption": Markup(
            "Nie chce ci się klepać adresu? Skanuj i wpadniesz na "
            f'<a href="{SITE["url"]}">{SITE["host"]}</a>.'
        ),
        "sticker_heading": "Naklejki",
        "sticker_lead": "Weź Gauguna ze sobą. Do domu.",
        "sticker_text": Markup(
            "Mamy naklejki. Przyklej na gitarę, lodówkę albo kurtkę z lumpeksu. "
            "Łap na koncercie albo napisz na "
            f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.'
        ),
        "sticker_alt": "Naklejka Gaugun",
    },
    "en": {
        "html_lang": "en",
        "other_lang": "pl",
        "other_path": "/",
        "switch_label": "Polski",
        "description": (
            "Four guys playing rock as if the last 30 years of music happened by accident."
        ),
        "bio": [
            Markup(
                "<strong>Gaugun</strong> is four guys playing rock as if the last 30 years "
                "of music happened by accident. A bit of classic rock, a bit of punk dirt, "
                "heavy riffs, and definitely too many amps. Influences? AC/DC, Black Sabbath, "
                "Pidżama Porno, and anything you can nod your head to while spilling your beer."
            ),
            (
                "We play loud, our way, with no extra fuss. If you like dirty guitars, "
                "straight-up lyrics, and gigs that leave your ears ringing a little "
                "— we'll probably get along."
            ),
        ],
        "links_heading": "Links",
        "contact_title": "Contact",
        "qr_alt": "QR code for the Gaugun website",
        "qr_caption": Markup(
            "Can't be bothered typing? Scan it and you're on "
            f'<a href="{SITE["url"]}">{SITE["host"]}</a>.'
        ),
        "sticker_heading": "Stickers",
        "sticker_lead": "Take Gaugun with you. Take him home.",
        "sticker_text": Markup(
            "We've got stickers. Stick one on a guitar, a fridge, or a thrift-store jacket. "
            "Grab one at a gig or drop a line to "
            f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.'
        ),
        "sticker_alt": "Gaugun sticker",
    },
}

LINKS = [
    {
        "title": "Facebook",
        "url": "https://www.facebook.com/gaugunband",
        "note": "@gaugunband",
        "icon": "facebook",
    },
    {
        "title": "Instagram",
        "url": "https://www.instagram.com/gaugun2137",
        "note": "@gaugun2137",
        "icon": "instagram",
    },
    {
        "title": "YouTube",
        "url": "https://www.youtube.com/@GAUGUN-piosenki",
        "note": "@GAUGUN-piosenki",
        "icon": "youtube",
    },
]

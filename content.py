from markupsafe import Markup

SITE = {
    "name": "Gaugun",
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
}

LINKS = [
    {
        "title": "Facebook",
        "url": "https://www.facebook.com/gaugunband",
        "note": "gaugunband",
    },
    {
        "title": "Instagram",
        "url": "https://www.instagram.com/gaugun2137",
        "note": "gaugun2137",
    },
    {
        "title": "YouTube",
        "url": "https://www.youtube.com/@GAUGUN-piosenki",
        "note": "GAUGUN-piosenki",
    },
]

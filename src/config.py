# config.py

import os
from dotenv import load_dotenv

load_dotenv()

URLS = {
    "GAME": "https://www.game.es/VIDEOJUEGOS/DEPORTES/PLAYSTATION-5/FIFA-22/191606",
    "MEDIAMARKT": "https://www.mediamarkt.es/es/product/_mando-sony-dualsense-v2-para-playstation-5-bluetooth-retroalimentacion-haptica-blanco-1565162.html",
    "ELCORTINGLES": "https://www.elcorteingles.es/videojuegos/A55296687-consola-nintendo-switch-2/"
}

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

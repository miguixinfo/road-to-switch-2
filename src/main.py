# main.py

import schedule
import time
from scraper import check_game_stock, check_mediamarkt_stock, check_elcorteingles_stock
from notifier import send_telegram_alert

def job():
    """
    Checks the stock availability of the Nintendo Switch at GAME store.

    This function prints a message indicating that it is checking the stock,
    calls the `check_game_stock` function to determine if the product is in stock,
    and sends a Telegram alert if the product is available. If the product is not
    available, it prints a message indicating that there is no stock.

    Returns:
        None
    """
    print("🔍 Comprobando stock en GAME...")
    in_stock, url = check_game_stock()
    # in_stock, url = check_mediamarkt_stock()
    # in_stock, url = check_elcorteingles_stock()
    if in_stock:
        send_telegram_alert(f"🎉 ¡STOCK DISPONIBLE en GAME! Corre: {url}")
    else:
        print("❌ No hay stock en GAME.")

schedule.every(60).seconds.do(job)

print("🕵️ Bot iniciado. Buscando stock...")

while True:
    schedule.run_pending()
    time.sleep(1)

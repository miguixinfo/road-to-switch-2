# scraper.py

import requests
from bs4 import BeautifulSoup
from config import URLS
from util import normalize_text

def check_game_stock():
    """
    Check if the Nintendo Switch is available in stock at GAME store.
    
    This function scrapes the GAME website to determine if the Nintendo Switch
    is currently available for purchase by looking for specific HTML elements
    that indicate stock availability or sold-out status.
    
    Returns:
        tuple: A tuple containing:
            - bool: True if the product is in stock, False otherwise
            - str or None: The product URL if in stock, None if not available
    """
    url = URLS["GAME"]
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    buy_span = soup.find("span", string=lambda s: s and "comprar" in normalize_text(s))
    buy_cart_span = soup.find("span", class_="icon iconGame ig-f-cart")

    sold_out = soup.find(string=lambda s: s and "agotado web" in normalize_text(s))

    if buy_span or buy_cart_span:
        return True, url
    elif sold_out:
        return False, None
    else:
        return False, None

    
# FIXME: Todavía no funciona, devuelve un captcha, ver en mediamarkt_debug.html
def check_mediamarkt_stock():
    """
    Check if the Nintendo Switch is available in stock at MediaMarkt store.
    
    This function scrapes the MediaMarkt website to determine if the Nintendo Switch
    is currently available for purchase. It looks for specific text patterns that
    indicate stock availability or unavailability. Currently has issues with
    CAPTCHA protection.
    
    Note:
        This function currently has issues with CAPTCHA protection and may not
        work reliably. It saves the HTML response to 'mediamarkt_debug.html'
        for debugging purposes.
    
    Returns:
        tuple: A tuple containing:
            - bool: True if the product is in stock, False otherwise
            - str or None: The product URL if in stock, None if not available
    """
    url = URLS["MEDIAMARKT"]
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    with open("mediamarkt_debug.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    soup = BeautifulSoup(response.content, "html.parser")
    
    available = any(
        "disponible online" in normalize_text(str(s))
        for s in soup.stripped_strings
    )
    if available:
        print("Hay texto de disponible")
    else:
        print("No hay texto de disponible")
    not_available = any(
        "este articulo no esta disponible actualmente" in normalize_text(str(s))
        for s in soup.stripped_strings
    )
    if not_available:
        print("Hay span de añadir al carrito")
    else:
        print("No hay span de añadir al carrito")
    
    if available and not not_available:
        return True, url
    else:
        return False, None
    
    
# FIXME: Todavía no funciona, se queda en un bucle
def check_elcorteingles_stock():
    """
    Check if the Nintendo Switch is available in stock at El Corte Inglés store.
    
    This function scrapes the El Corte Inglés website to determine if the Nintendo Switch
    is currently available for purchase by looking for specific button elements that
    indicate stock availability or sold-out status.
    
    Note:
        This function currently has issues and may get stuck in a loop.
        The implementation needs to be reviewed and fixed.
    
    Returns:
        tuple: A tuple containing:
            - bool: True if the product is in stock, False otherwise
            - str or None: The product URL if in stock, None if not available
    """
    url = URLS["ELCORTINGLES"]
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    not_stock_button = soup.find("button", string=lambda s: s and "agotado" in s.lower())
    stock_button = soup.find("button", string=lambda s: s and "añadir a la cesta" in s.lower())
    
    if not_stock_button:
        return False, None
    elif stock_button:
        return True, url
    else:
        return False, None
    


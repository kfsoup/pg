import sys
import requests
import re
from urllib.parse import urljoin


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return.
    Relativní odkazy se doplní na úplné URL.
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Chybový status kod: {response.status_code}")

        html = response.text
        hrefs_raw = re.findall(r'href="([^"]+)"', html)

        # doplníme relativní odkazy na úplné URL
        hrefs = [urljoin(url, h) for h in hrefs_raw]

        return hrefs

    except Exception as e:
        print(f"Chyba při stahování URL: {e}")
        return []


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise Exception("Nebyl zadán URL! Spusťte program: python sixth.py https://www.jcu.cz")

        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)

        # vypíšeme všechny odkazy
        for h in hrefs:
            print(h)

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
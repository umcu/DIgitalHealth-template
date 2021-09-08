import bs4
import logging
from os.path import join
import requests

from src.config import DATA_DIR, UCI_HEART_DISEASE_URL


def download_directory_from_url(url) -> None:
    """Download a directory with data from a url.

    Parameters
    ----------
    url : str
        Url of the directory to be downloaded
    """
    r = requests.get(url)
    data = bs4.BeautifulSoup(r.text, "html.parser")

    for line in data.find_all("a"):
        r = requests.get(url + line["href"])
        logging.info(f"Downloading file: {line['href']} (status code: {r.status_code})")
        if r.status_code == 200:
            path = join(DATA_DIR, "raw", line["href"])
            if path[-1] == "/":
                continue
            with open(path, "wb") as f:
                f.write(r.content)

    assert "hello"


if __name__ == "__main__":
    download_directory_from_url(UCI_HEART_DISEASE_URL)

import requests
from base import Fetcher


def get_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        raise RuntimeError(f"Could not fetch {url}") from error

    response.encoding = "utf-8"
    return response.text


class SecondSourceFetcher(Fetcher):
    def fetch(self,url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as error:
            raise RuntimeError(f"Could not fetch {url}") from error

        response.encoding = "utf-8"
        return response.text

    
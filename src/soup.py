import re
import urllib.request

from bs4 import BeautifulSoup


class Soup:
    """ Use beautiful soup library to get item data """
    def __init__(self, uri):
        req = urllib.request.Request(
            uri,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'  # noqa
            }
        )
        with urllib.request.urlopen(req) as response:
            html = response.read()
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_title(self):
        try:
            return self.soup.find(
                'meta', {'property': 'og:title'}
            ).attrs['content']
        except (KeyError, AttributeError,):
            return self.soup.head.title.text

    def get_image(self):
        try:
            return self.soup.find(
                'meta', {'property': 'og:image'}
            ).attrs['content']
        except (KeyError, AttributeError,):
            return

    def get_price(self, only_number=True):
        for elem in self.soup.findAll(
            attrs={'id': re.compile('price', re.IGNORECASE)}
        ):
            if only_number:
                try:
                    return re.findall(r'[0-9.,]+', elem.text)[0]
                except IndexError:
                    pass
            else:
                if elem.text:
                    return elem.text
        return

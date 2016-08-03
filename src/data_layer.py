import json
import re


class DataLayer:
    """
    Class to parse html and search for JS dataLayer variable initialization,
    since usually it contains some of the item data
    """
    def __init__(self, soup):
        self.data_layer = dict()
        for script in soup.findAll("script"):
            script_text = script.text
            if re.search(r'dataLayer[ ]*=[ ]*\[', script_text):
                m = re.search(
                    r'{.*}', script_text,
                    re.IGNORECASE | re.MULTILINE | re.DOTALL
                )
                self.data_layer = json.loads(re.sub(
                    '\'', '\"', ''.join(script_text[m.start():m.end()].split())
                ))

    def _get_item(self, default_tag, *tag_regexps):
        for tag in self.data_layer:
            if re.search(default_tag, tag, re.IGNORECASE):
                default_data = self.data_layer[tag]
                break
        else:
            return

        for filter_tag in [default_tag, *tag_regexps, ]:
            tags = list(filter(
                lambda key: re.search(filter_tag, key),
                self.data_layer
            ))
            if len(tags) == 1:
                return self.data_layer[tags[0]]

        return default_data

    def get_price(self):
        return self._get_item(
            'price',
            re.compile('^(current.*price|price.*current)$', re.IGNORECASE),
            re.compile('^(product.*price|price.*product)$', re.IGNORECASE),
            re.compile('current.*price|price.*current', re.IGNORECASE),
            re.compile('product.*price|price.*product', re.IGNORECASE),
        )

    def get_image(self):
        return self._get_item(
            'image',
            'img',
            re.compile('^(image.*ur(l|i)|ur(l|i).*image)$', re.IGNORECASE),
            re.compile('image.*ur(l|i)|ur(l|i).*image', re.IGNORECASE),
            re.compile('^(img.*ur(l|i)|ur(l|i).*img)$', re.IGNORECASE),
            re.compile('img.*ur(l|i)|ur(l|i).*img', re.IGNORECASE),
        )

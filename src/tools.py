import json

from src.data_layer import DataLayer
from src.soup import Soup


def get_product_info(uri, clean_price=True):
    soup = Soup(uri)
    data_layer = DataLayer(soup.soup)
    return {
        'uri': uri,
        'title': soup.get_title(),
        'img': soup.get_image() or data_layer.get_image(),
        'price': data_layer.get_price() or soup.get_price(
            only_number=clean_price
        ),
    }


def get_products_info(uris, clean_price):
    product_data = []
    for uri in uris:
        product_data.append(get_product_info(uri, clean_price=clean_price))
    return product_data


def pretty_print(data):
    # Results may contain unicode which will be escaped after json.dumps()
    print(
        bytearray(
            json.dumps(data, indent=4, sort_keys=True), 'utf-8'
        ).decode('unicode_escape')
    )

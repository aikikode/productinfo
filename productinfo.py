#!/usr/bin/env python3

import argparse

from src.tools import get_products_info, pretty_print

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Get key information about a product from a web store page'
    )
    parser.add_argument(
        '--numeric-price', '-n', dest='clean_price', action='store_true',
        help='Provide price as a number without any text'
    )
    parser.add_argument(
        'urls', nargs='+', help='product URL from the web store'
    )
    args = parser.parse_args()
    pretty_print(get_products_info(args.urls, args.clean_price))

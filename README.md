# productinfo

Get key information like title, price and image about a product from a web store page given the page URL

## Requirements
`python3`, `python3-virtualenv`

## Installation
Create Python virtiualenv and install dependencies

```bash
make venv
```

## Usage
```bash
productinfo.py [-h] [--numeric-price] url [url ...]

positional arguments:
  url                 product URL from the web store

optional arguments:
  -h, --help           show this help message and exit
  --numeric-price, -n  Provide price as a number without any text
```
Example
```bash
source venv/bin/activate
./productinfo.py https://www.jcrew.com/ru/womens_category/shoes/sandals/PRDOVR\~A4966/A4966.jsp
[
    {
        "img": "https://i.s-jcrew.com/is/image/jcrew/A4966_YL5596?$pdp_fs418$",
        "price": "124.99",
        "title": "Studded lace-up gladiator sandals",
        "uri": "https://www.jcrew.com/ru/womens_category/shoes/sandals/PRDOVR~A4966/A4966.jsp"
    }
]
```

Some shops provide price in local currency, the app will try to find the price in original currency, but even then the original currency may change from site to site. So the default behaviour of the app is to provide the full price text including the currency sign (name) and details, e.g.:
```bash
./productinfo.py http://www.ebay.com/itm/SOG-Outdoor-Survival-Tool-Lock-Stainless-Steel-Saber-Folding-Blade-Knife-/222167544871
[
    {
        "img": "http://i.ebayimg.com/images/i/222167544871-0-1/s-l1000.jpg",
        "price": "333,49 руб.(включая доставку)",
        "title": "SOG Outdoor Survival Tool Lock Stainless Steel Saber Folding Blade Knife",
        "uri": "http://www.ebay.com/itm/SOG-Outdoor-Survival-Tool-Lock-Stainless-Steel-Saber-Folding-Blade-Knife-/222167544871"
    }
]
```
If you need only the numeric representation of the price, use `--numeric-price` flag:
```bash
./productinfo.py --numeric-price http://www.ebay.com/itm/SOG-Outdoor-Survival-Tool-Lock-Stainless-Steel-Saber-Folding-Blade-Knife-/222167544871
[
    {
        "img": "http://i.ebayimg.com/images/i/222167544871-0-1/s-l1000.jpg",
        "price": "333,49",
        "title": "SOG Outdoor Survival Tool Lock Stainless Steel Saber Folding Blade Knife",
        "uri": "http://www.ebay.com/itm/SOG-Outdoor-Survival-Tool-Lock-Stainless-Steel-Saber-Folding-Blade-Knife-/222167544871"
    }
]
```

## Unistall
```bash
make clean
```

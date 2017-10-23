## Description

This is a simple app to fetch historical UF values from Banco Central de Chile. It works on BeautifulSoup, Selenium and PhantomJS.

## Installation

Install python packages:
    pip install -r requirements.txt

Install PhantomJS:
    Follow instructions from https://gist.github.com/julionc/7476620

## Use

Fetch UF historical data:
    python manage.py shell
    from uf.views import scrape_uf
    scrape_uf()

Run app:
    python manage.py runserver

Check results:
    http://127.0.0.1:8000/uf/list
    http://127.0.0.1:8000/uf/price?value=25&date=19981021




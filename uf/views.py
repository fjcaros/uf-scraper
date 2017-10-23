# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from uf.models import Price
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import date


# Create your views here.


def list(request):
    prices = Price.objects.all().order_by('-date')
    context = {'prices': prices}
    return render(request, 'uf/list.html', context)


def price(request):
    uf = float(request.GET.get('value', ''))
    d = request.GET.get('date', '')

    year = int(d[0:4])
    month = int(d[4:6])
    day = int(d[6:8])
    d = date(year, month, day)

    p = Price.objects.get(date=d)
    result = uf * p.value
    # print result

    context = {'result': result, 'p': p}
    return render(request, 'uf/price.html', context)


def scrape_uf():
    if Price.objects.all().count() == 0:
        url = 'http://si3.bcentral.cl/Indicadoressiete/secure/Serie.aspx?gcode=UF&param=RABmAFYAWQB3AGYAaQBuAEkALQAzADUAbgBNAGgAaAAkADUAVwBQAC4AbQBYADAARwBOAGUAYwBjACMAQQBaAHAARgBhAGcAUABTAGUAYwBsAEMAMQA0AE0AawBLAF8AdQBDACQASABzAG0AXwA2AHQAawBvAFcAZwBKAEwAegBzAF8AbgBMAHIAYgBDAC4ARQA3AFUAVwB4AFIAWQBhAEEAOABkAHkAZwAxAEEARAA%3d'
        driver = webdriver.PhantomJS()
        driver.get(url)
        current_year = 2017
        end_year = 1977

        while current_year >= end_year:
            select = Select(driver.find_element_by_id('DrDwnFechas'))
            select.select_by_visible_text(str(current_year))
            # driver.save_screenshot(str(current_year) + '.png')
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            table = soup.find(id='gr')
            rows = table.find_all('tr')

            for row in rows:
                data = row.find_all('td')

                if data:
                    day = int(data[0].string)

                    for idx, value in enumerate(data):
                        if idx > 0:
                            if value.string:
                                uf = float(value.string.replace('.', '').replace(',', '.'))
                                d = date(current_year, idx, day)
                                p = Price(value=uf, date=d)
                                p.save()
                                print p

            current_year -= 1


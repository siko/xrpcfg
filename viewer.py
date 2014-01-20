#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Usage :
#   install the requiremnts,modfiy the wcg account id of the wcgid below.
#   pip install lxml
#   pip install requests
#   pip install beautifulsoup4
#
# Author : Siko Chen <sikocb@gmail.com>
# Donate : Ripple address : r3zJeqaGN3NeHqHufNypUGnnjahJKnKMAJ

import requests
import datetime
from bs4 import BeautifulSoup

def getpoint(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.text)

    rows = soup.find('table').findAll('tr')[1:]
    for row in rows:
        columns = [data.text for data in row.findAll('td')[0:-1]]
        todays = datetime.datetime.now().strftime('%b %d, %Y')
        if columns[0] == todays:
            print columns[0]+'\t\t'+columns[1]+'\t\t'+columns[2]

cfgurl = 'https://www.computingforgood.org/stats/member/'
wcgid = [866331,868931,864681]

for w in wcgid:
    getpoint(cfgurl+str(w))



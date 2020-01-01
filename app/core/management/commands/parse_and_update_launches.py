import requests as req
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from core.models import Launch


class Command(BaseCommand):
  help = "Parses Roscosmos website for launches and updates DB"

  def __init__(self, *args, **kwargs):
    super.__init__(*args, **kwargs)
    self.URL = "https://www.roscosmos.ru/launch/2019/"

  def handle(self, *args, **options):
    resp = req.get(self.URL)
    soup = BeautifulSoup(resp.text, 'lxml')

    # parse web page
    table = soup.find('table', class_='table-launch')
    launches = []

    for tr in table.find_all('tr'):
      temp_launch = {
        'date': None,
        'name': None,
        'pad': None,
        'vehicle': None,
        'result': None,
      }

      for td in tr.find_all('td'):
        if 'pusk-date' in td['class']:
          temp_launch['date'] = td.string
        if 'pusk-name' in td['class']:
          temp_launch['name'] = td.string
        if 'pusk-place' in td['class']:
          temp_launch['pad'] = td.string
        if 'pusk-rn' in td['class']:
          temp_launch['vehicle'] = td.string
        if 'pusk-result' in td['class']:
          temp_launch['result'] = td.string
        else:
          pass

      if temp_launch['date'] != None:
        launches.append(temp_launch)

    # put parsed data into

import requests as req
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from core.models import Launch, LaunchPad, LaunchVehicle, ParseUrl, ParserLaunch

from ._utils import filter_parsed_launch_list, correct_launch_list, fetch_date, fetch_time, fetch_result, correct_time


class Command(BaseCommand):
  help = "Parses Roscosmos website for launches and updates DB"

  def handle(self, *args, **options):
    for urlobj in ParseUrl.objects.all():
      resp = req.get(urlobj.url)
      soup = BeautifulSoup(resp.text, 'lxml')

      # parse web page
      table = soup.find('table', class_='table-launch')
      launches = []

      for tr in table.find_all('tr'):
        temp_launch = {
          'no': None,
          'date': None,
          'time': '',
          'name': None,
          'pad': None,
          'vehicle': None,
          'result': None,
        }

        for td in tr.find_all('td'):
          if 'pusk-nn' in td['class']:
            temp_launch['no'] = td.string
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

        launches.append(temp_launch)

      launches = filter_parsed_launch_list(launches)
      launches = correct_launch_list(launches, fetch_date, fetch_time, fetch_result)
      launches.sort(key=lambda el: int(el['no']))

      try:
        latest_launch_no = ParserLaunch.objects.filter(url__url=urlobj.url).latest('parse_date').last_saved_launch_no
      except:
        latest_launch_no = 0

      if latest_launch_no <= len(launches):
        last_saved_launch_no = 0

        for i in range(latest_launch_no, len(launches)):
          if launches[i]['time'] == '':
            corrected_time = None
          else:
            corrected_time = correct_time(launches[i]['time'])

          try:
            launch = Launch(
              name = launches[i]['name'],
              date = launches[i]['date'],
              time = corrected_time,
              result = launches[i]['result'],
              launch_pad = LaunchPad.objects.get(name=launches[i]['pad']),
              launch_vehicle = LaunchVehicle.objects.get(name=launches[i]['vehicle']),
            )
            launch.save()
            last_saved_launch_no = launches[i]['no']
          except:
            pass

        no_launches_saved = len(launches) - latest_launch_no
        if no_launches_saved > 0:
          parser_launch = ParserLaunch(url=urlobj, no_launches=no_launches_saved, last_saved_launch_no=last_saved_launch_no)
          parser_launch.save()

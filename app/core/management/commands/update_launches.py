import requests as req
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from core.models import (Launch,
                         LaunchPad,
                         LaunchVehicle,
                         ParseUrl,
                         ParserLaunch)
from ._utils import (filter_parsed_launch_list,
                     correct_and_sort_launch_list,
                     fetch_date,
                     fetch_time,
                     fetch_result,
                     correct_time)


class Command(BaseCommand):
  help = "Parses Roscosmos website for launches and updates DB"

  def handle(self, *args, **options):
    for urlobj in ParseUrl.objects.all():
      resp = req.get(urlobj.url)
      soup = BeautifulSoup(resp.text, 'html.parser')

      table = soup.find('table', class_='table-launch')
      launches = []

      for tr in table.find_all('tr'):
        temp_launch = {'time': None}

        for td in tr.find_all('td'):
          if 'pusk-nn' in td['class']:
            temp_launch['no'] = td.string
          elif 'pusk-date' in td['class']:
            temp_launch['date'] = td.string
          elif 'pusk-name' in td['class']:
            temp_launch['name'] = td.string
          elif 'pusk-place' in td['class']:
            temp_launch['pad'] = td.string
          elif 'pusk-rn' in td['class']:
            temp_launch['vehicle'] = td.string
          elif 'pusk-result' in td['class']:
            temp_launch['result'] = td.string

        launches.append(temp_launch)

      launches = filter_parsed_launch_list(launches)
      launches = correct_and_sort_launch_list(
        launches, fetch_date, fetch_time, fetch_result)

      try:
        last_launch_no = ParserLaunch.objects.filter(
          url__url=urlobj.url).latest('parse_date').last_saved_launch_no
      except:
        last_launch_no = 0

      if last_launch_no < len(launches):
        no_launches_saved = 0
        last_saved_launch_no = 0

        for i in range(last_launch_no, len(launches)):
          try:
            launch = Launch(
              name=launches[i]['name'],
              date=launches[i]['date'],
              time=correct_time(launches[i]['time']),
              result=launches[i]['result'],
              launch_pad=LaunchPad.objects.get(name=launches[i]['pad']),
              launch_vehicle=LaunchVehicle.objects.get(
                name=launches[i]['vehicle']),
            )
            launch.save()

            no_launches_saved += 1
            last_saved_launch_no = int(launches[i]['no'])
          except:
            pass

        if no_launches_saved > 0:
          parser_launch = ParserLaunch(
            url=urlobj,
            no_launches_saved=no_launches_saved,
            last_saved_launch_no=last_saved_launch_no,
          )
          parser_launch.save()

import re


def fetch_date(date_time_line):
  try:
    uncorrected_date = date_time_line.split(' ')[0]
    uncorrected_date_list = re.split(r'\.|\:', uncorrected_date)
    correct_date = f'{uncorrected_date_list[2]}-'\
                   f'{uncorrected_date_list[1]}-{uncorrected_date_list[0]}'

    return correct_date
  except:
    return None


def fetch_time(date_time_line):
  try:
    correct_time = date_time_line.split(' ')[1]

    return correct_time
  except:
    return None


def correct_time(time_line):
  if (isinstance(time_line, str) and len(time_line) == 5
     and time_line.count(':') == 1):
    time_line = f'{time_line}:00'

  return time_line


def fetch_result(result_line):
  correct_result = None

  if result_line == 'Успешный':
    correct_result = 'SUCCESS'
  elif result_line == 'Неуспешный':
    correct_result = 'FAILED'
  elif result_line == 'Предстоящий':
    correct_result = 'UPCOMING'
  elif result_line == 'Аварийный':
    correct_result = 'EMERGENCY'

  return correct_result


def filter_parsed_launch_list(parsed_launch_list):
  for el in parsed_launch_list:
    if len(el.values()) != 7:
      parsed_launch_list.remove(el)

  return parsed_launch_list


def correct_and_sort_launch_list(launch_list, fetch_date,
                                 fetch_time, fetch_result):
  for el in launch_list:
    date = el['date']
    el['date'] = fetch_date(date)
    el['time'] = fetch_time(date)
    el['result'] = fetch_result(el['result'])

  launch_list.sort(key=lambda el: int(el['no']))

  return launch_list

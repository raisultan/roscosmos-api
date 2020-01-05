import requests as req
from bs4 import BeautifulSoup
from celery import shared_task

from django.core import management

@shared_task
def update_launches():
  try:
    print ('IN CELERY MODULE')
    management.call_command('update_launches')
    return 'SUCCESSFULLY UPDATED'
  except Exception as e:
    print(e)

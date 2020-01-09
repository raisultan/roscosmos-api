from django.http import HttpResponse


def index(request):
  return HttpResponse("<a href='https://github.com/Raysultan/roscosmos-api'>\
    <h3>link to roscosmos api github</h3></a>")

from django.http import HttpResponse


def index(request):
  return HttpResponse("<pre>Роскосмос API!</pre>\
        <pre>Docs: https://documenter.getpostman.com/view/6866794/SWLh5Rqu</pre>\
        <pre>GitHub: https://github.com/Raysultan/roscosmos-api</pre>\
        <pre>Роскосмос: https://www.roscosmos.ru/</pre>")

from django.http import HttpResponse


def index(request):
  return HttpResponse("<pre>Роскосмос API!\
        Docs: https://documenter.getpostman.com/view/2025350/RWaEzAiG\
        GitHub: https://github.com/Raysultan/roscosmos-api\
        Роскосмос: https://www.roscosmos.ru/</pre>")

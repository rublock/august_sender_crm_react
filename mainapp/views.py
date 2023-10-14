from django.http import HttpResponse


def home_page(request):
    response = HttpResponse("Привет из Djnango")
    return response
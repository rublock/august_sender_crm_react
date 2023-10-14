from django.http import HttpResponse


def home_page(request):
    response = HttpResponse("Привет из Djnango")
    return response


def signin_page(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    response = HttpResponse(f"Привет {email} c паролем {password}")
    return response

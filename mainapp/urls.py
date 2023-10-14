from django.urls import path

from mainapp import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("signin/", views.signin_page, name="signin_page"),
]

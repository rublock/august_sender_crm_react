from django.urls import path
from .views import ClientList

urlpatterns = [
    path("", ClientList.as_view(), name="get_clients_data"),
]

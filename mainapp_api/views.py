from rest_framework import generics, permissions
from mainapp.models import Client
from .serializers import ClientSerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAdminUser,)

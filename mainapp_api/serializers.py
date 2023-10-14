from rest_framework import serializers
from mainapp.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "contact",
            "where_from",
            "oder_details",
            "address",
            "notes",
            "created_at",
            "updated_at",
        )
        model = Client
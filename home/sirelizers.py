from rest_framework import serializers
from .models import CarsModel


class CarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = "__all__"

from rest_framework import serializers
from .models import Driver

class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
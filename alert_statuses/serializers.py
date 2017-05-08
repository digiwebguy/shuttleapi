from rest_framework import serializers
from .models import AlertStatus

class AlertStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertStatus
        fields = '__all__'
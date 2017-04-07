from rest_framework import serializers
from .models import Timestamp

class TimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timestamp
        fields = '__all__'
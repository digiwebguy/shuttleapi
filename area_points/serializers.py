from rest_framework import serializers
from .models import AreaPoint

class AreaPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaPoint
        fields = '__all__'
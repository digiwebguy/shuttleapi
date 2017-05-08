from rest_framework import serializers
from .models import DirectionOption

class DirectionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionOption
        fields = '__all__'
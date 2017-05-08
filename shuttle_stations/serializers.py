from rest_framework import serializers
from .models import ShuttleStation
from area_points.serializers import AreaPointSerializer
from direction_options.serializers import DirectionOptionSerializer

class ShuttleStationSerializer(serializers.ModelSerializer):
    area_points = AreaPointSerializer(many=True)
    direction_options = DirectionOptionSerializer(many=True)
    class Meta:
        model = ShuttleStation
        fields = ('id', 'name', 'area_points', 'direction_options')
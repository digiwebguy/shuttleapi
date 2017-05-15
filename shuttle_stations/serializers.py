from rest_framework import serializers
from .models import ShuttleStation
from direction_options.serializers import DirectionOptionSerializer
from direction_options.serializers import DirectionOptionWithAlertsSerializer
from area_points.serializers import AreaPointSerializer
from alerts.serializers import AlertSerializer


class ShuttleStationSerializer(serializers.ModelSerializer):
    area_points = AreaPointSerializer(many=True)
    direction_options = DirectionOptionSerializer(many=True)

    class Meta:
        model = ShuttleStation
        fields = ('id', 'name', 'area_points', 'direction_options', 'alerts')


class ShuttleStationAlertsSerializer(serializers.ModelSerializer):
    # alerts = AlertSerializer(many=True, read_only=True)
    direction_options = DirectionOptionWithAlertsSerializer(many=True)

    class Meta:
        model = ShuttleStation
        fields = ('id', 'name', 'direction_options')


from rest_framework import serializers
from .models import DirectionOption
from alerts.serializers import AlertSerializer


class DirectionOptionSerializer(serializers.ModelSerializer):


    class Meta:
        model = DirectionOption
        fields = ('id','option', "shuttle_station_id")


class DirectionOptionWithAlertsSerializer(serializers.ModelSerializer):
    alerts = AlertSerializer(many=True, read_only=True)
    shuttle_station_name = serializers.SlugRelatedField(source="shuttle_station_id", read_only=True, slug_field="name" )

    class Meta:
        model = DirectionOption
        fields = ('id','option', "shuttle_station_id", "alerts", "shuttle_station_name")

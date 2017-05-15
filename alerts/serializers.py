from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    shuttle_station_name = serializers.SlugRelatedField(source="shuttle_station_id", slug_field="name", read_only=True)
    direction = serializers.SlugRelatedField(source="direction_id", slug_field="option", read_only=True)

    class Meta:
        model = Alert
        fields = ('id', 'alert_time', "shuttle_station_id", "shuttle_station_name", "direction_id", "direction")
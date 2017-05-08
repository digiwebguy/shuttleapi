from rest_framework import serializers
from .models import ShuttleLocation

class ShuttleLocationSerializer(serializers.ModelSerializer):
    driver_name = serializers.SlugRelatedField(many=False, source="driver_id", slug_field='firstname', read_only=True)
    class Meta:
        model = ShuttleLocation
        fields = ('lat', 'lng', 'driver_name', 'driver_id')
from django.db import models
from shuttle_stations.models import ShuttleStation

class AreaPoint(models.Model):
    order_position = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    shuttle_station_id = models.ForeignKey(ShuttleStation, related_name="area_points")

    def __str__(self):
        title = 'Point %s for %s' % (self.order_position, self.shuttle_station_id)
        return title
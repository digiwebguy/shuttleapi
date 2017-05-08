from django.db import models
from shuttle_stations.models import ShuttleStation

class DirectionOption(models.Model):
    shuttle_station_id = models.ForeignKey(ShuttleStation, related_name="direction_options", blank=True, null=True)
    option = models.CharField(max_length=100)

    def __str__(self):
        title = "%s %s" % (self.shuttle_station_id, self.option)
        return title

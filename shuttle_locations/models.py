from django.db import models
from drivers.models import Driver

class ShuttleLocation(models.Model):
    driver_id = models.ForeignKey(Driver, related_name='shuttle_locations')
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        title = "%s  (%s, %s)" %(self.driver_id, self.lat, self.lng)
        return title

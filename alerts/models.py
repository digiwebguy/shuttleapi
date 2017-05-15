from django.db import models
from users.models import User
from drivers.models import Driver
from shuttle_stations.models import ShuttleStation
from direction_options.models import DirectionOption
from alert_statuses.models import AlertStatus

class Alert(models.Model):
    user = models.ForeignKey(User)
    shuttle_station_id = models.ForeignKey(ShuttleStation, related_name="alerts")
    direction_id = models.ForeignKey(DirectionOption, related_name="alerts")
    alert_time = models.DateTimeField()
    driver_accepted_id = models.ForeignKey(Driver, null=True, blank=True)
    accepted_time = models.DateTimeField(null=True, blank=True)
    status_id = models.ForeignKey(AlertStatus, related_name="alerts", default='1')

    def __str__(self):
        title = "%s %s %s" %(self.alert_time, self.shuttle_station_id, self.direction_id)
        return title

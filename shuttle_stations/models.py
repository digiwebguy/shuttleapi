from django.db import models

class ShuttleStation(models.Model):
    area_points = ForeignKey(AreaPoint, related_name="shuttle_stations")
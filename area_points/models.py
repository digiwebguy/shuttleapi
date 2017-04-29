from django.db import models

class AreaPoint(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

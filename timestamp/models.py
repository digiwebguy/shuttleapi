from django.db import models

class Timestamp(models.Model):
    current_time = models.DateTimeField()
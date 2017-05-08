from django.db import models

class AlertStatus(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

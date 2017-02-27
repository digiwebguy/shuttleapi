from django.db import models

class Trip(models.Model):
    datetime = models.DateTimeField()
    user_id = models.BigIntegerField()
    pickup_location = models.CharField(max_length=20)

    def __str__(self):
        return self.pickup_location + " " + self.datetime;

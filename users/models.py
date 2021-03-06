from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    index_number = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.firstname

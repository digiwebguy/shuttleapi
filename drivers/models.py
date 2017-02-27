from django.db import models

class Driver(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname

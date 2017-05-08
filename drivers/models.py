from django.db import models

class Driver(models.Model):
    car_number = models.CharField(max_length=10, default='')
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        title = "%s %s %s" % (self.car_number, self.firstname, self.lastname)
        return title

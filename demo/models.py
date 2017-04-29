from django.db import models

class Demo(models.Model):
    light_status = models.BooleanField()



    def __str__(self):
        return str(self.light_status)
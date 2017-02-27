from django.db import models

class Topup(models.Model):
    datetime = models.DateTimeField()
    user_id = models.BigIntegerField()
    amoount = models.FloatField()
    payment_type = models.CharField(max_length=3)
    phone_number = models.IntegerField()
    network = models.CharField(max_length=3)
    voucher_code = models.CharField(max_length=12)#this might change

    def __str__(self):
        return self.user_id + " " + self.amount;

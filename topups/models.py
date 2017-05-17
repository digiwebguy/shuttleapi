from django.db import models
from vouchers.models import Voucher
from datetime import datetime

class Topup(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    user_id = models.BigIntegerField()
    amount = models.FloatField()
    payment_type = models.CharField(max_length=3)
    phone_number = models.IntegerField(null=True, blank=True)
    network = models.CharField(max_length=3, null=True, blank=True)
    voucher_id = models.ForeignKey(Voucher, related_name="topups", null=True, blank=True )


    # def __str__(self):
        # return self.user_id + " " + self.amount
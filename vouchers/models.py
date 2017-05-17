from django.db import models


class Voucher(models.Model):
    voucher_code = models.CharField(max_length=12)
    is_active = models.BooleanField(default=1)
    amount = models.IntegerField(default=1)

    def __str__(self):
        title = "Voucher: %s |  isActive: %s" % (self.voucher_code, self.is_active)
        return title

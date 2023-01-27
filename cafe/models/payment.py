from django.db import models

from cafe.models.reservation import Reserve


class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    total = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    ref_id = models.TextField(null=True, blank=True)
    tx_id = models.TextField(null=True, blank=True)


class PaymentReserve(Payment):
    reservation = models.ForeignKey(Reserve, on_delete=models.CASCADE)

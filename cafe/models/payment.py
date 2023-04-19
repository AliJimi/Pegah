from django.db import models

from cafe.models.reservation import Reserve
from django.contrib.sessions.models import Session


class Payment(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total = models.PositiveIntegerField(blank=False, null=False)
    is_paid = models.BooleanField(default=False)
    discount = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    phone_number = models.PositiveIntegerField(blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    ref_id = models.TextField(null=True, blank=True)
    tx_id = models.TextField(null=True, blank=True)


class PaymentReserve(Payment):
    reservation = models.ForeignKey(Reserve, on_delete=models.CASCADE)


class PymentCourse(Payment):
    need_delivery = models.BooleanField(blank=False, default=False)
    need_table = models.BooleanField(blank=False, default=True)
    is_done = models.BooleanField(blank=False, default=False)
    start_date = models.DateTimeField(blank=False, null=True)
    is_accepted = models.BooleanField(blank=False, null=True)
    address = models.TextField(blank=False, null=True)

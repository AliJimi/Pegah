from django.contrib.sessions.models import Session
from django.db import models

from cafe.models.course import Course


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(blank=False, null=False, default=True)
    final_price = models.PositiveIntegerField(blank=False, null=True)
    discount = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    order = models.TextField(blank=False, null=True, default=None)
    is_canceled = models.BooleanField(blank=False, default=True)
    is_done = models.BooleanField(blank=False, default=False)
    start_date = models.DateTimeField(blank=False, null=True)
    is_accepted = models.BooleanField(blank=False, null=True)
    need_delivery = models.BooleanField(blank=False, default=False)
    need_table = models.BooleanField(blank=False, default=True)
    description = models.TextField(blank=False, null=True)
    phone_number = models.PositiveIntegerField(blank=False, null=True)

    def to_json(self):
        orders_id = self.order.split(',')
        order = dict()
        for order_row in orders_id:
            course = Course.objects.get()

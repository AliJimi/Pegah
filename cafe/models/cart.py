from django.contrib.sessions.models import Session
from django.db import models

from cafe.models.course import Course


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def to_json(self):
        pass


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    occupation = models.PositiveIntegerField()

    is_available = models.BooleanField(default=True)
    is_reserved = models.BooleanField(default=False)
    is_occupied = models.BooleanField(default=False)

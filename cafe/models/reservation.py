from django.db import models

from cafe.models.table import Table


class Reserve(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    count = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

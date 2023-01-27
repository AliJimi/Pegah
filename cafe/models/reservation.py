from django.db import models

from cafe.models.table import Table


class Reserve(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

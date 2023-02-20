import uuid as uuid
from django.db import models

from cafe.models.table import Table


class Reserve(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now_add=True)

    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    count = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.uuid,
            'created_at': self.created_at.strftime('%Y/%M/%d, %H:%m:%s'),
            'count': self.count,
            'name': self.name
        }

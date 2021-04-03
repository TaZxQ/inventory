"""
All Django Models for Inventory items data
"""

from django.db import models
from miniproject.batch.models import Batch


class Item(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    item_date = models.DateTimeField(null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=False, related_name="items")

    class Meta:
        db_table = 'Item'

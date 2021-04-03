# Django imports
from django.db import models
from miniproject.user.models import UserAccount


class Batch(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    vendor_name = models.TextField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    batch_date = models.DateTimeField(null=True)
    manager = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=False, related_name="batch_manager")

    class Meta:
        db_table = 'Batch'

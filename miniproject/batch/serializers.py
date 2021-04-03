# Local imports
# Django imports
from django.core.paginator import EmptyPage, Paginator
# RestFramework imports
from rest_framework import serializers

from .models import Batch


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('id', 'name', 'description', 'vendor_name', 'created_at', 'batch_date', 'manager',)

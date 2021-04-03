from .models import UserAccount
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'city', 'state']

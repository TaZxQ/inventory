from .models import UserAccount
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'city', 'state']

    def create(self, validated_data):
        # get random password here to send email to new user
        random_password = self.Meta.model.objects.make_random_password()
        print(random_password)
        validated_data['password'] = make_password(random_password)
        return super(UserSerializer, self).create(validated_data)

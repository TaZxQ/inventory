from .models import UserAccount
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from sendgrid import Mail, Cc, SendGridAPIClient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'city', 'state']

    def create(self, validated_data):
        # get random password here to send email to new user
        random_password = self.Meta.model.objects.make_random_password()

        # sendgrid API integration to send the managers their password on sign up

        message = Mail(
            from_email=('mian.waqashafiz@gmail.com', 'mini inventory'),
            to_emails='mian.waqashafiz@gmail.com',
            subject='Sending with Twilio SendGrid is Fun',
            html_content=f'<strong>Your password is {random_password}</strong>')
        try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

        validated_data['password'] = make_password(random_password)
        return super(UserSerializer, self).create(validated_data)

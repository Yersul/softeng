from datetime import date

from django.contrib.auth.models import User
from rest_framework import serializers

from timee.models import Timee, CHOICES


class TimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timee
        fields = (
            'id',
            'user',
            'action_in',
            'date_in',
            'time_in',
            'action_out',
            'date_out',
            'time_out'
        )


class TimeCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Timee
        fields = (
            'user',
            'action_in',
            'date_in',
            'time_in',

        )


class TimeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timee
        fields = (
            'user',
            'action_out',
            'date_out',
            'time_out'
        )
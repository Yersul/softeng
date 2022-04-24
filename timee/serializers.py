from django.contrib.auth.models import User
from rest_framework import serializers


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user',
            'action_in',
            'time_in',
            'action_out',
            'time_out'
        )


class TimeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user',
            'action_in',
            'time_in',
        )


class TimeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user',
            'action_out',
            'time_out'
        )
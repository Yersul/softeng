from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

CHOICES = [
    ('in', 'зашел'),
    ('out', 'вышел'),
]


class Timee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_date = date.today()
    action_in = models.CharField(max_length=5, choices=CHOICES, default='in')
    date_in = models.DateField(auto_now_add=True)
    time_in = models.TimeField(auto_now_add=True)
    action_out = models.CharField(max_length=5, choices=CHOICES, default='out')
    date_out = models.DateField(auto_now_add=True)
    time_out = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = 'Выбрать время'
        ordering = ['user']

    def __str__(self):
        return str(self.user)

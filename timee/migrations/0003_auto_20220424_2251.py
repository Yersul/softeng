# Generated by Django 3.2.12 on 2022-04-24 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timee', '0002_auto_20220422_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timee',
            name='action_in',
            field=models.CharField(choices=[('in', 'зашел'), ('out', 'вышел')], default='in', editable=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='timee',
            name='action_out',
            field=models.CharField(choices=[('in', 'зашел'), ('out', 'вышел')], default='out', editable=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='timee',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.12 on 2022-04-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timee',
            name='action',
        ),
        migrations.AddField(
            model_name='timee',
            name='action_in',
            field=models.CharField(choices=[('in', 'зашел'), ('out', 'вышел')], default='in', max_length=5),
        ),
        migrations.AddField(
            model_name='timee',
            name='action_out',
            field=models.CharField(choices=[('in', 'зашел'), ('out', 'вышел')], default='out', max_length=5),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsApp', '0004_days_dayschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='otp',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]

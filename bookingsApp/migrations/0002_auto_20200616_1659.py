# Generated by Django 3.0.7 on 2020-06-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

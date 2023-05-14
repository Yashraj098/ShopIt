# Generated by Django 4.1.7 on 2023-05-13 21:35

import datetime
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0016_cart_dprice_orders_dprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='qty',
        ),
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=phone_field.models.PhoneField(default=0, max_length=31),
        ),
        migrations.AddField(
            model_name='orders',
            name='timeplaced',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 13, 21, 35, 18, 400870, tzinfo=datetime.timezone.utc)),
        ),
    ]
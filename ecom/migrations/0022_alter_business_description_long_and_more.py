# Generated by Django 4.1.7 on 2023-05-19 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0021_alter_business_description_short_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='description_long',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_long',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='timeplaced',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 14, 32, 56, 170381, tzinfo=datetime.timezone.utc)),
        ),
    ]

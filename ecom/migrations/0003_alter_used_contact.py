# Generated by Django 4.1.7 on 2023-04-15 10:47

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_alter_used_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='used',
            name='contact',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]

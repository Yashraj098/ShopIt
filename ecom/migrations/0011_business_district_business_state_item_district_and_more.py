# Generated by Django 4.1.7 on 2023-04-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0010_business_remove_item_contact_remove_item_gst_req_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='district',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='business',
            name='state',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='district',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='state',
            field=models.CharField(default='', max_length=20),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0012_business_user_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]

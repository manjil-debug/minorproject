# Generated by Django 3.1.7 on 2021-05-08 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_auto_20210508_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_requests',
            name='request_date',
        ),
    ]

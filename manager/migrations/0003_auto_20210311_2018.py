# Generated by Django 3.1.1 on 2021-03-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_customer_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_requests',
            name='ph_number',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 3.1.2 on 2021-03-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_customer_requests'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('ph_number', models.IntegerField()),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]

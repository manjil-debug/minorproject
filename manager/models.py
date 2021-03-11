from django.db import models
# Create your models here.


class venu(models.Model):
    name=models.CharField(max_length=200)
    booking_price=models.IntegerField()

    def __str__(self):
        return self.name


class customer_requests(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)
    ph_number = models.IntegerField(max_length=10)
    email = models.EmailField()
    venue = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    per_request = models.TextField(max_length=500)

    def __str__(self):
        return self.name




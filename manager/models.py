from django.db import models
# Create your models here.


class venu(models.Model):
    name=models.CharField(max_length=200)
    booking_price=models.IntegerField()
    veg_pricing = models.IntegerField()
    nonveg_pricing =models.IntegerField()
    h_drinks =models.IntegerField()

    def __str__(self):
        return self.name


class customer_requests(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)
    ph_number = models.IntegerField()
    email = models.EmailField()
    venue = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    per_request = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class customer_register(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    u_name = models.CharField(max_length=200)
    email = models.EmailField()
    ph_number = models.IntegerField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.f_name





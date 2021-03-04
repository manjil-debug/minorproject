from django.db import models
# Create your models here.

class venu(models.Model):
    name=models.CharField(max_length=200)
    booking_price=models.IntegerField()

    def __str__(self):
        return self.name
    

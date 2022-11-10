from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length = 30) 
    discount_percentage = models.PositiveIntegerField()
    currency = models.CharField(max_length = 3)
    
from django.db import models

# Create your models here.

class Service(models.Model):
    serviceno=models.IntegerField()
    servicename=models.CharField(max_length=64)
    servicerate=models.FloatField()



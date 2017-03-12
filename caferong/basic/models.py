from django.db import models

# Create your models here.
class Cafe(models.Model):
    name = models.CharField(max_length=30)
    time = models.CharField(max_length=100)
    locLat = models.FloatField(default=0)
    locLng = models.FloatField(default=0)
    Roastery = models.CharField(max_length=5, default='N')
    Engname = models.CharField(max_length=10)
    #picture = models.ImageField()
    #comment = models.CharField(max_length=200)

from django.db import models

# Create your models here.

class Heartrate(models.Model):
    BPM = models.IntegerField()
    RESP = models.IntegerField()
    time = models.DateTimeField()
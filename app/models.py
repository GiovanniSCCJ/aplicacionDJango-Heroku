"""
Definition of models.
"""

from django.db import models

class publisher(models.Model):
    date = models.IntegerField()
    dateString = models.DateTimeField()
    rssi = models.IntegerField()
    device = models.CharField( max_length=20 )
    direction = models.CharField( max_length=20 )
    rawbg = models.IntegerField()
    sgv = models.IntegerField()
    type = models.CharField( max_length=20 )
    utcoffset = models.IntegerField()
    sysTime = models.DateTimeField()

# Create your models here.

#"date": Number,
#    "dateString": Date,
#    "rssi": Number,
#    "device": String,
#    "direction": String,
#    "rawbg": Number,
#    "sgv": Number,
#    "type": String,
#    "utcOffset": Number,
#    "sysTime": Date

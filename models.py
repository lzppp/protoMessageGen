from django.db import models
from enum import Enum
# Create your models here.
#request
class RequestCommon(models.Model):
    userid = models.IntegerField()
    userkey = models.CharField(max_length = 30)
    cmdid = models.IntegerField()
    timestamp = models.DateField()
    version =  models.CharField(max_length = 30)
    platform = models.IntegerField()

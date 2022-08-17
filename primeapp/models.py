from django.db import models
import datetime

# Create your models here.
class Savedata(models.Model):
    startno=models.IntegerField(default=0)
    stopno=models.IntegerField(default=0)
    outdata1=models.TextField(default=None)
    outdata2=models.TextField(default=None)
    time=models.DateTimeField()

    def __str__(self):
        return id

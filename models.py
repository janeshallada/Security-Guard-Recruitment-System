from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Guards(models.Model):
    user1=models.CharField(max_length=100, null=True, blank=True)
    guardname=models.CharField(max_length=100, null=True, blank=True)
    firstname=models.CharField(max_length=100, null=True, blank=True)
    lastname=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    mobileno=models.CharField(max_length=100, null=True, blank=True)
    age=models.CharField(max_length=100, null=True, blank=True)
    gender=models.CharField(max_length=100, null=True, blank=True)
    idtype=models.CharField(max_length=100, null=True, blank=True)
    idnumber=models.CharField(max_length=100, null=True, blank=True)
    qualification=models.CharField(max_length=100, null=True, blank=True)
    pic=models.FileField(upload_to="media/",max_length=300, null=True, blank=True)
    address=models.CharField(max_length=100, null=True, blank=True)
    passphoto=models.FileField(upload_to="media/",max_length=300, null=True, blank=True)
    status=models.CharField(max_length=100,default="Not Updated Yet", null=True, blank=True)
    remark=models.CharField(max_length=100, null=True, blank=True)
    level=models.CharField(max_length=100, default="not get any training Level", null=True, blank=True)
    rlevel=models.CharField(max_length=100, null=True, blank=True)
    issue=models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.lastname
    
class Trackinghistory(models.Model):
    guard = models.ForeignKey(Guards, on_delete=models.CASCADE, null=True, blank=True)
    remark = models.CharField(max_length=100, default="Not Updated Yet", null=True, blank=True)
    status = models.CharField(max_length=100, default="Not Updated Yet", null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    workplace=models.CharField(max_length=100,default="work not assigned", null=True, blank=True)
    contactno=models.CharField(max_length=100, default="1234506789", null=True, blank=True)
    fromtime=models.CharField(max_length=100, null=True, blank=True)
    totime=models.CharField(max_length=100, null=True, blank=True)
    fromdate=models.DateTimeField(null=True, blank=True)
    todate=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.remark

class Training(models.Model):
    guard2 = models.ForeignKey(Guards, on_delete=models.CASCADE, null=True, blank=True)
    tstatus = models.CharField(max_length=100, default="Not Updated Yet", null=True, blank=True)
    location=models.CharField(max_length=100,default="Training not assigned", null=True, blank=True)
    contactno2=models.CharField(max_length=100, default="1234506789", null=True, blank=True)
    fromtime=models.CharField(max_length=100, null=True, blank=True)
    totime=models.CharField(max_length=100, null=True, blank=True)
    fromdate=models.DateTimeField(null=True, blank=True)
    todate=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.location
    
    
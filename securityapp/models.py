from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Guard(models.Model):
    guardname = models.CharField(max_length=100, null=True, blank=True)
    mobilenumber = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    idtype = models.CharField(max_length=100, null=True, blank=True)
    idnumber = models.CharField(max_length=100, null=True, blank=True)
    pic = models.FileField(null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.guardname

class Booking(models.Model):
    guardname = models.ForeignKey(Guard, on_delete=models.CASCADE, null=True, blank=True)
    bookingnumber = models.CharField(max_length=100, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobileno = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    requirementnumber = models.CharField(max_length=100, null=True, blank=True)
    shift = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    fromdate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, default="Not Updated Yet", null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    guardassign = models.CharField(max_length=100, null=True, blank=True)
    fromdate = models.DateField(null=True, blank=True)
    todate = models.DateField(null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname

class Trackinghistory(models.Model):
    guardname = models.ForeignKey(Guard, on_delete=models.CASCADE, null=True, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    remark = models.CharField(max_length=100, default="Not Updated Yet", null=True, blank=True)
    status = models.CharField(max_length=100, default="Not Updated Yet", null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.remark
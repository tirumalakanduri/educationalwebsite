from django.db import models

# Create your models here.

class Registration(models.Model):
    rname=models.CharField(max_length=150)
    rphone=models.IntegerField(max_length=150)
    remail=models.CharField(max_length=150)
    rstudentname=models.CharField(max_length=150)
    rmessage=models.CharField(max_length=150)

    def __str__(self):
        return self.rname

class Contactreg(models.Model):
    cname = models.CharField(max_length=150)
    cphone=models.IntegerField(max_length=150)
    cemail=models.CharField(max_length=150)
    cmessage=models.CharField(max_length=150)

    def __str__(self):
        return self.cname


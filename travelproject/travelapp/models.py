from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Members(models.Model):
    membrname=models.CharField(max_length=200)
    membrimg=models.ImageField(upload_to='pics')
    membrdesc=models.TextField()


    # def __str__(self):
    #     return self.name
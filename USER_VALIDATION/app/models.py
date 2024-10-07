from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=200)
    pno = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    add = models.CharField(max_length=200)
    un = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
from django.db import models
from django.db import  models
# Create your models here.
class Product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=30)
    pcost=models.DecimalField(max_digits=10,decimal_places=4)
    pmfd=models.DateField()
    pexpdt=models.DateField()

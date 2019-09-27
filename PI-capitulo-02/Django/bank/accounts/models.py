from django.db import models

# Create your models here.
class Account(models.Model):
    owner = models.CharField(max_length=50)
    balance = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)

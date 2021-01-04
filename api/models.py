from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)
    price = models.IntegerField()
    reference = models.CharField(max_length=9)
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

class userdetails(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)
    message=models.CharField(max_length=70)
    


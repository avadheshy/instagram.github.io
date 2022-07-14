from django.db import models


# Create your models here.
class user(models.Model):
    user_data=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

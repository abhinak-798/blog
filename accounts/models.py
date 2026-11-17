from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustumUser(AbstractUser):
    phone_no=models.CharField(max_length=10)
    bio=models.TextField()
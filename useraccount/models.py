from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    UserRole=(
        ('admin','Admin'),
        ('host','Host'),
        ('user','User'),
        
    )
    role=models.CharField(max_length=10,choices=UserRole,default='user')

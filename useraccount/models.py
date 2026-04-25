from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    UserRole=(
        ('user','User'),
        ('host','Host'),
        ('admin','Admin'),
    )
    role=models.CharField(max_length=10,choices=UserRole,default='user')

    def __str__(self):
        return self.role
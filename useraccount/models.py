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
    is_host_approved=models.BooleanField(default=False)

class HostRequest(models.Model):
    HostStatus=(
        ("approved","Approved"),
        ("rejected","Rejected"),
        ("pending","Pending"),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=HostStatus, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"


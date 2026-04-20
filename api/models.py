from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} product"
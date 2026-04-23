from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filterset_fields=['category']
    filter_backends=[OrderingFilter,SearchFilter,DjangoFilterBackend]
    search_fields=['name']
    ordering_fields=['created_at','price']
    permission_classes=[IsAuthenticatedOrReadOnly]
   


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Product.objects.filter(user=self.request.user)
        return Product.objects.all()
    
    



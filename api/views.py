from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import IsHost,IsAdmin,IsOwnerOrAdmin

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filterset_fields=['category']
    filter_backends=[DjangoFilterBackend,OrderingFilter,SearchFilter]
    search_fields=['name']
    ordering_fields=['price','created_at']


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            if user.role=="host":
                return Product.objects.filter(user=user)
            elif user.role=="admin":
                return Product.object.all()
        return Product.objects.all()

    def get_permission(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsHost()]
        elif self.action in ['update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return [AllowAny()]
        
        



    
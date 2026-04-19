from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
    filterset_fields=['category']
    filter_backends=[OrderingFilter,SearchFilter]
    ordering_fields=['created_at','category']
    search_fields=['name','price']
    permission_classes=[IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        print("DATA RECEIVED:", request.data)
        return super().create(request, *args, **kwargs)
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['category']
    search_fields=['name','price']
    ordering_fields=['price']
    permission_classes=[IsAuthenticatedOrReadOnly]

    # def create(self, request, *args, **kwargs):
    #     print("DATA RECEIVED:", request.data)
    #     return super().create(request, *args, **kwargs)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Product.objects.filter(user=self.request.user)
        else:
            return Product.objects.all()


    
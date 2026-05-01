from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product
from useraccount.permissions import IsAdmin,IsHost,IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    #Not Scalabel
    '''
    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            if user.role=="host":
                return Product.objects.filter(user=user)
            if user.role=="admin":
                return Product.objects.all()
        return Product.objects.all()

    '''
    #Scalable
    def get_queryset(self):
        user = self.request.user
        #Public users
        if not user.is_authenticated:
            return Product.objects.all()
        
        #High Level Access Code:
        if user.role=='admin' or user.is_staff or user.is_superuser:
            return Product.objects.all()

        
        #Code Extention of High level access(user.role='admin' or user.is_staff or user.is_superuser:)
        '''
        if user.is_superuser:
            return Products.objects.all()

        if user.is_staff:
            return Products.objects.all()

        if user.role == 'admin':
            return Product.objects.all()
        '''
        # Host → own products
        if user.role == 'host':
            return Product.objects.filter(user=user)

        # Normal user
        if user.role == 'user':
            return Product.objects.filter()
            #use this if you only want to show approved Listings/Public Listings:
            '''
            return Product.objects.filter(is_published=True):
            '''


        #is a safety net, Without it the queryset function may return nothing = app crash
        return Product.objects.all()

    def get_permissions(self):
        if self.action=='create':
            return [IsAuthenticated(),IsHost()]
        if self.action in ['update','destroy']:
            return [IsAuthenticated(),IsOwnerOrAdmin()]
        elif self.action == 'admin_only_action':
            return [IsAuthenticated(), IsAdmin()]
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [AllowAny()]

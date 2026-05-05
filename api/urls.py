from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,ListingViewSet

router=DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('listing',ListingViewSet,basename='listing')

urlpatterns=router.urls
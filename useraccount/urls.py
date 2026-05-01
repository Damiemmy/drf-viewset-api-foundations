from django.urls import path
from .views import RegisterAPIView,UserRoleViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('roles',UserRoleViewSet,basename='roles')

urlpatterns=[
    path('register/',RegisterAPIView.as_view(),name='register')
]

urlpatterns += router.urls
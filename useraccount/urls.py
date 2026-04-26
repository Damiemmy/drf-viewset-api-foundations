from .views import RegisterViewSet,UserRoleViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('roles',UserRoleViewSet,basename='roles')

urlpatterns=[
    path('register',RegisterViewSet.as_view(),name='register')
]

urlpatterns += router.urls



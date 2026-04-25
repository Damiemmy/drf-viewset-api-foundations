from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
# Create your views here.

class RegisterViewSet(CreateAPIView):
    serializer_class=RegisterSerializer

class UserRoleViewSet(ViewSet):
    permission_classes=[IsAuthenticated]

    @action(detail=False, methods=['post'])
    def become_host(self,request):
        user=request.user
        user.role='host'
        user.save()
        return Response({"message":"you are now a host"})



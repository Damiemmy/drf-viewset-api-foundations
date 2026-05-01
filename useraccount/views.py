from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class RegisterAPIView(CreateAPIView):
    serializer_class=RegisterSerializer


class UserRoleViewSet(ViewSet):
    @action(detail=False,methods=['post'])
    def become_host(self,request):
        user=request.user
        user.role='host'
        user.save()
        return Response({"message":"You are now a Host"})
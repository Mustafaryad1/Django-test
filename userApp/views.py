from rest_framework import viewsets
from rest_framework.response import Response
from userApp import (
    serializers,
    models,
)
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = models.User.objects.all()
  serializer_class = serializers.UserSerializer

  

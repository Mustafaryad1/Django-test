from userApp.models import User
from rest_framework import serializers
from productApp.models import Product,Category

class UserSerializer(serializers.ModelSerializer):
  categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'email','categories',]

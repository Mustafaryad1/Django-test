from productApp.models import Product, Category, Settings
from rest_framework import serializers


class SettingsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Settings
    fields = ['id', 'main_system_currency',]


class CategorySerializer(serializers.ModelSerializer):
  admin = serializers.ReadOnlyField(source='admin.username')

  class Meta:
    model = Category
    fields = ['id', 'count','sold','default_price','type','admin','products','total_revenue']
    depth = 1
  
  def perform_create(self, serializer):
    serializer.save(admin=self.request.user)


class ProductSerializer(serializers.ModelSerializer):
  category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
      )

  class Meta:
    model = Product
    fields = ['id', 'title','price','category','category_id','purchased_at','buyer']
    depth= 1


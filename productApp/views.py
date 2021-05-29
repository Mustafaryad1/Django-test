from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Sum

from productApp.permissions import IsOwnerOrReadOnly
from productApp import (
    serializers,
    models,
)
# Create your views here.

class SettingsViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = models.Settings.objects.all()
  serializer_class = serializers.SettingsSerializer

  
class CategoryViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = models.Category.objects.all()
  serializer_class = serializers.CategorySerializer

  
class ProductViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = models.Product.objects.all()
  serializer_class = serializers.ProductSerializer

  
class PurchasedProducts(APIView):
  permission_classes = [permissions.IsAuthenticated,]

  def get(self,request):
    purchased_products = models.Product.objects.filter(
      purchased_at__isnull=False
    )

    items = []
    for item in purchased_products:
      items.append(item.to_json())

    return Response({"data":items})


class BuyItem(APIView):

  def post(self,request):
    permission_classes = [permissions.IsAuthenticated,]
    product_id = request.data.get('product_id')
    if product_id:
      founded = models.Product.objects.filter(id=product_id)
      if founded:
        product = founded[0]
        if product.purchased_at:
          
          return Response({"message":"this product sold "})
        else:
          product.buyer_id = request.user.id
          product.purchased_at = timezone.now()
          product.category.total_revenue += product.price
          product.category.save()
          product.save()
          return Response({"message":"success","data":product.to_json()})

   
    return Response({"data":"not found"},status=404)


class OwnPurchasedProducts(APIView):
  permission_classes = [permissions.IsAuthenticated,]
  def get(self, request):
    purchased_products = models.Product.objects.filter(
      buyer_id=request.user.id,
    )

    items = []
    for item in purchased_products:
      items.append(item.to_json())

    return Response({"data":items})


class TotalRevenue(APIView):
  permission_classes = [permissions.IsAuthenticated,]
  
  def get(self, request):
    total_revenue = models.Product.objects.filter(
      purchased_at__isnull=False
    ).aggregate(Sum('price'))

    return Response({"data":total_revenue})
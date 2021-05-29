from django.urls import path, include
from rest_framework.routers import DefaultRouter
from productApp import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'settings', views.SettingsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('purchased-products/', views.PurchasedProducts.as_view()),
    path('total-revenue/', views.TotalRevenue.as_view()),
    path('buy-item/', views.BuyItem.as_view()),
    path('own-items/', views.OwnPurchasedProducts.as_view()),
]
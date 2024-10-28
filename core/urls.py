from django.urls import path, include
from django.db import router
from rest_framework import routers
from . import views





router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'address', views.AddressViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'orderStatus', views.OrderStatusViewSet)
router.register(r'productImage', views.ProductImageViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderLine', views.OrderLineViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'cartItem', views.CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]

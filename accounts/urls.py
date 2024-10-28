from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'accounts', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet
from madameParfum.views import contact_us


# router = routers.DefaultRouter()
# router.register(r'accounts', UserViewSet)

urlpatterns = [
    path('contact_us/', contact_us, name='contact-us')
]

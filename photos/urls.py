from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet

# Router automatically generates URLs
router = DefaultRouter()
router.register(r"photos", PhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

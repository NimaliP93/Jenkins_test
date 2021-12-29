from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import PackageModelViewSet

router = DefaultRouter()
router.register(r'package', PackageModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


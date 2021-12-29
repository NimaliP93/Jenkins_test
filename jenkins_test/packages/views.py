from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Package
from .serializers import PackageSerializer


class PackageModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

#pylint: disable=no-member
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CategoriaMaterial, Material
from .serializers import CategoriaMaterialSerializer, MaterialSerializer

class CategoriaMaterialViewSet(viewsets.ModelViewSet):
    queryset = CategoriaMaterial.objects.all()
    serializer_class = CategoriaMaterialSerializer
    permission_classes = [IsAuthenticated]


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

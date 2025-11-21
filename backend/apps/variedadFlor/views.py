#pylint: disable=no-member
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TypeVariedadFlor, VariedadFlor
from .serializers import TypeVariedadFlorSerializer, VariedadFlorSerializer

class TypeVariedadFlorViewSet(viewsets.ModelViewSet):
    queryset = TypeVariedadFlor.objects.all()
    serializer_class = TypeVariedadFlorSerializer
    permission_classes = [IsAuthenticated]


class VariedadFlorViewSet(viewsets.ModelViewSet):
    queryset = VariedadFlor.objects.all()
    serializer_class = VariedadFlorSerializer
    permission_classes = [IsAuthenticated]

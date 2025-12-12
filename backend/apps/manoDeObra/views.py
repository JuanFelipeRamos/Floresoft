#pylint: disable=no-member
from rest_framework import viewsets
from .models import ManoDeObra, CostoVariedadTinturar
from .serializers import ManoDeObraSerializer, CostoVariedadTinturarSerializer

class ManoDeObraViewSet(viewsets.ModelViewSet):
    queryset = ManoDeObra.objects.all()
    serializer_class = ManoDeObraSerializer


class CostoVariedadTinturarViewSet(viewsets.ModelViewSet):
    queryset = CostoVariedadTinturar.objects.all()
    serializer_class = CostoVariedadTinturarSerializer

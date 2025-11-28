#pylint: disable=no-member
from rest_framework import viewsets
from .models import ManoDeObra
from .serializers import ManoDeObraSerializer

class ManoDeObraViewSet(viewsets.ModelViewSet):
    queryset = ManoDeObra.objects.all()
    serializer_class = ManoDeObraSerializer

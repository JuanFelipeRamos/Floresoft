from rest_framework.generics import CreateAPIView
from .models import UsuarioAdministrador
from .serializers import UsuarioAdminSerializer

class UsuarioAdminViewSet(CreateAPIView):
    queryset = UsuarioAdministrador.objects.all()
    serializer_class = UsuarioAdminSerializer

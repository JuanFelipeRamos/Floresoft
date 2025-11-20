from django.urls import path
from .views import UsuarioAdminViewSet


urlpatterns = [
    path("register/", UsuarioAdminViewSet.as_view(), name="register-usuarios")
]

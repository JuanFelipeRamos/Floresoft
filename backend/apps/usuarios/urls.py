from django.urls import path
from .views import UsuarioAdminViewSet, MsgRecuperarPwdView


urlpatterns = [
    path("register/", UsuarioAdminViewSet.as_view(), name="register-usuarios"),
    path("mensaje_recuperar_pwd/", MsgRecuperarPwdView.as_view(), name="mensaje-recuperar-pwd")
]

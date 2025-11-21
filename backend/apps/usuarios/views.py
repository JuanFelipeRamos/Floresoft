from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import UsuarioAdministrador
from .serializers import UsuarioAdminSerializer

# Vista para crear usuarios
class UsuarioAdminViewSet(CreateAPIView):
    queryset = UsuarioAdministrador.objects.all()
    serializer_class = UsuarioAdminSerializer


#---Función para obtener el email enviado, buscar ese usuario, pasar su ID a base64 y generarle un token ------------->
User = get_user_model()

def obtener_usuario(request):
    email_user = request.data.get('email')

    try:
        usuario = User.objects.get(email=email_user)
    except User.DoesNotExist:
        return None

    uid = urlsafe_base64_encode(force_bytes(usuario.pk))
    token = default_token_generator.make_token(usuario)

    return {
        'email_user': email_user,
        'username': usuario.username,
        'uid': uid,
        'token': token
    }
#--------------------------------------------------------------------------------------->

# Enviar mensaje (por email) para recuperar contraseña (estableciendo una nueva)
class MsgRecuperarPwdView(APIView):
    def post(self, request):
        datos_usuario = obtener_usuario(request)

        if not datos_usuario:
            return Response({
                "error": "Usuario no encontrado"
            }, status=status.HTTP_404_NOT_FOUND)

        verification_url = f"http://localhost:5173/AddNewPwd?uidb64={datos_usuario['uid']}&token={datos_usuario['token']}"

        email = EmailMessage(
            subject = "Recupera tu contraseña de Floresoft",
            body = f"""
            <h1>Hola {datos_usuario['username']}</h1>
            <p>Has solicitado recuperar tu contraseña. Haz clic en el siguiente enlace para ingresar una nueva contraseña:</p>
            <a href="{verification_url}">Ingresar nueva contraseña</a>
            <p><strong>NOTA:</strong> Si no fuiste tú quien solicitó esta acción, por favor ignora este mensaje.</p>
            """,
            from_email = settings.EMAIL_HOST_USER,
            to = [datos_usuario['email_user']]
        )
        email.content_subtype = "html"

        try:
            respuesta = email.send()

            if respuesta == 1:
                return Response({
                    "message": "email enviado exitosamente"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": "error al enviar el email"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(f"Error al enviar el correo: {str(e)}")
            return Response({
                "error": "Error inesperado al intentar enviar el correo"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

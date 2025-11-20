from django.contrib.auth.models import AbstractUser

class UsuarioAdministrador(AbstractUser):
    """
    username (obligatorio)
    first_name
    last_name
    email
    password
    is_staff
    is_active
    is_superuser
    date_joined
    last_login
    """

    def __str__(self):
        return f"{self.username, self.email}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

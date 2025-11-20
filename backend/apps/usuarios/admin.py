from django.contrib import admin
from .models import UsuarioAdministrador

@admin.register(UsuarioAdministrador)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "last_login")

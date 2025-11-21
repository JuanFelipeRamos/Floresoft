from django.contrib import admin
from .models import TypeVariedadFlor, VariedadFlor

@admin.register(TypeVariedadFlor)
class TypeVariedadFlorAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(VariedadFlor)
class VariedadFlorAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "type_flor")

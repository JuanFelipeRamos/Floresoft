from django.contrib import admin
from .models import CategoriaMaterial, Material

@admin.register(CategoriaMaterial)
class CategoriaMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "categoria")

from django.contrib import admin
from .models import ManoDeObra, CostoVariedadTinturar

@admin.register(ManoDeObra)
class ManoDeObraAdmin(admin.ModelAdmin):
    list_display = ("name", "cost_per_hour")

@admin.register(CostoVariedadTinturar)
class CostoVariedadTinturarAdmin(admin.ModelAdmin):
    list_display = ("name_variedad", "price")

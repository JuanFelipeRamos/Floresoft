from django.contrib import admin
from .models import ManoDeObra

@admin.register(ManoDeObra)
class ManoDeObraAdmin(admin.ModelAdmin):
    list_display = ("name", "cost_per_hour")

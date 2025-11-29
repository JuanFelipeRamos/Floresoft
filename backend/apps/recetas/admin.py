from django.contrib import admin
from .models import Receta, MaterialReceta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = (
        'num_receta',
        'get_variedades',
        'total_variedades',
        'get_materiales',
        'total_materiales'
        )

    def get_materiales(self, obj):
        # Muestra todos los materiales conectados a la receta
        materiales = obj.materialreceta_set.all()
        return ", ".join([mr.material.name for mr in materiales])

    get_materiales.short_description = "Materiales"

    def get_variedades(self, obj):
        # Muestra todas las variedades conectados a la receta
        variedades = obj.variedadflorreceta_set.all()
        return ", ".join([mr.variedad.name for mr in variedades])

    get_variedades.short_description = "Variedades"

@admin.register(MaterialReceta)
class MaterialRecetaAdmin(admin.ModelAdmin):
    list_display = ("material", "receta", "quantity")

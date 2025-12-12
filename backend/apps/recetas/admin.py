from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = (
        'num_receta',
        'get_variedades',
        'total_variedades',
        'get_materiales',
        'total_materiales',
        'get_manos_de_obra',
        'total_mano_de_obra'
        )

    def get_variedades(self, obj):
        # Muestra todas las variedades conectados a la receta
        variedades = obj.variedadflorreceta_set.all()
        return ", ".join([mr.variedad.name for mr in variedades])

    get_variedades.short_description = "Variedades"


    def get_materiales(self, obj):
        # Muestra todos los materiales conectados a la receta
        materiales = obj.materialreceta_set.all()
        return ", ".join([mr.material.name for mr in materiales])

    get_materiales.short_description = "Materiales"


    def get_manos_de_obra(self, obj):
        # Muestra todas las manos de obra conectados a la receta
        manos_de_obra = obj.manodeobrareceta_set.all()
        return ", ".join([mr.manodeobra.name for mr in manos_de_obra])

    get_manos_de_obra.short_description = "Manos de obra"

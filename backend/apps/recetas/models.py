from django.db import models
from apps.variedadFlor.models import VariedadFlor
from apps.materiales.models import Material
from apps.manoDeObra.serializers import ManoDeObra

class Receta(models.Model):
    num_receta = models.PositiveIntegerField()
    quantity_bouquets = models.PositiveIntegerField()
    quantity_stems_for_bouquets = models.PositiveIntegerField()

    variedades = models.ManyToManyField(VariedadFlor, through="VariedadFlorReceta")
    total_variedades = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)

    materiales = models.ManyToManyField(Material, through="MaterialReceta")
    total_materiales = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    manos_de_obra = models.ManyToManyField(ManoDeObra, through="ManoDeObraReceta")
    total_mano_de_obra = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.num_receta} - {self.materiales} - {self.total_materiales}"

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"


# Tabla intermedia receta-variedades
class VariedadFlorReceta(models.Model):
    variedad = models.ForeignKey(VariedadFlor, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    quantity_stems_of_variety = models.PositiveIntegerField()
    style_stems = models.CharField(max_length=15)
    price_total_tallos = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)


# Tabla intermedia receta-materiales
class MaterialReceta(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_total = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Material de la receta"
        verbose_name_plural = "Materiales de recetas"


# Tabla intermedia receta-manos de obra
class ManoDeObraReceta(models.Model):
    mano_de_obra = models.ForeignKey(ManoDeObra, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    price_total = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

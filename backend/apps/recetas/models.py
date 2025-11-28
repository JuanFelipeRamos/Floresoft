from django.db import models
from apps.materiales.models import Material
from apps.variedadFlor.models import VariedadFlor

class Receta(models.Model):
    num_receta = models.PositiveIntegerField()
    materiales = models.ManyToManyField(Material, through="MaterialReceta")
    total_materiales = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.num_receta} - {self.materiales} - {self.total_materiales}"

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"


# Tabla intermedia receta-variedades
class VariedadFlorReceta(models.Model):
    variedad = models.ForeignKey(VariedadFlor, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    quantity_stems = models.PositiveIntegerField()
    quantity_bouquets = models.PositiveIntegerField()
    price_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)


# Tabla intermedia receta-materiales
class MaterialReceta(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_total = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Material de la receta"
        verbose_name_plural = "Materiales de recetas"

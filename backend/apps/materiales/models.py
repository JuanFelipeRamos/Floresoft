from django.db import models

class CategoriaMaterial(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría del material"
        verbose_name_plural = "Categorías de los materiales"


class Material(models.Model):
    name = models.CharField(max_length=40, unique=True)
    categoria = models.ForeignKey(CategoriaMaterial, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

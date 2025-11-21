from django.db import models

class TypeVariedadFlor(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de variedad de flor"
        verbose_name_plural = "Tipos de variedades de flores"


class VariedadFlor(models.Model):
    name = models.CharField(max_length=30, unique=True)
    type_flor = models.ForeignKey(TypeVariedadFlor, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "Variedad de flor"
        verbose_name_plural = "Variedades de flores"

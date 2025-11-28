from django.db import models

class ManoDeObra(models.Model):
    name = models.CharField(max_length=25)
    cost_per_hour = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.cost_per_hour}"

    class Meta:
        verbose_name = "Mano de obra"
        verbose_name_plural = "Manos de obra"

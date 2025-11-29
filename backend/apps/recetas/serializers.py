#pylint: disable=no-member
from rest_framework import serializers
from .models import Receta, MaterialReceta, VariedadFlorReceta
from apps.materiales.models import Material
from apps.materiales.serializers import MaterialSerializer
from apps.variedadFlor.models import VariedadFlor
from apps.variedadFlor.serializers import VariedadFlorSerializer

class VariedadFlorRecetaSerializer(serializers.Serializer):
    variedad = serializers.CharField()
    quantity_stems = serializers.IntegerField(min_value=1)
    quantity_bouquets = serializers.IntegerField(min_value=1)

    class Meta:
        model = VariedadFlorReceta
        fields = "__all__"

    def validate_variedad(self, value):
        try:
            variedad = VariedadFlor.objects.get(name=value)
        except VariedadFlor.DoesNotExist as exc:
            raise serializers.ValidationError({
                "error": "la variedad ingresada no existe"
            }) from exc

        return variedad


# serializer para listar las variedades con detalles en la lista de variedades de una receta
class VariedadFlorRecetaReadSerializer(serializers.ModelSerializer):
    variedad = VariedadFlorSerializer(read_only=True)
    class Meta:
        model = VariedadFlorReceta
        fields = ["id", "variedad", "quantity_stems", "quantity_bouquets", "price_total_tallos"]


class MaterialRecetaSerializer(serializers.Serializer):
    material = serializers.CharField()
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = MaterialReceta
        fields = "__all__"

    def validate_material(self, value):
        try:
            material = Material.objects.get(name=value)
        except Material.DoesNotExist as exc:
            raise serializers.ValidationError({
                "error": "el material ingresado no existe"
            }) from exc

        return material


# serializer para listar los materiales con detalles en la lista de materiales de una receta
class MaterialRecetaReadSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)
    class Meta:
        model = MaterialReceta
        fields = ["id", "material", "quantity", "price_total"]


class RecetaSerializer(serializers.ModelSerializer):
    detalles_variedad = VariedadFlorRecetaSerializer(many=True, write_only=True) # lista de variedades
    variedades = VariedadFlorRecetaReadSerializer(source="variedadflorreceta_set", many=True, read_only=True)

    detalles_material = MaterialRecetaSerializer(many=True, write_only=True) # lista de materiales
    materiales = MaterialRecetaReadSerializer(source="materialreceta_set", many=True, read_only=True)

    class Meta:
        model = Receta
        fields = [
            "num_receta",
            "detalles_variedad",
            "variedades",
            "total_variedades",
            "detalles_material",
            "materiales",
            "total_materiales"
            ]

    def create(self, validated_data):
        detalles_v = validated_data.pop("detalles_variedad")
        detalles_m = validated_data.pop("detalles_material")
        receta = Receta.objects.create(**validated_data)

        total_v = 0
        total_m = 0

        # recorrer lista de variedades----------------------------------------------------
        for i in detalles_v:
            variedad = i["variedad"]
            quantity_stems = i["quantity_stems"]
            quantity_bouquets = i["quantity_bouquets"]

            precio_tallos_por_ramo = variedad.price * quantity_stems
            precio_variedad_en_total_ramos = precio_tallos_por_ramo * quantity_bouquets
            total_v += precio_variedad_en_total_ramos

            VariedadFlorReceta.objects.create(
                variedad = variedad,
                receta = receta,
                quantity_stems = quantity_stems,
                quantity_bouquets = quantity_bouquets,
                price_total_tallos = precio_variedad_en_total_ramos
            )

        # recorrer lista de materiales----------------------------------------------------
        for i in detalles_m:
            material = i["material"]
            quantity = i["quantity"]

            precio_total = material.price * quantity
            total_m += precio_total

            MaterialReceta.objects.create(
                material = material,
                receta = receta,
                quantity = quantity,
                price_total = precio_total
            )

        receta.total_variedades = total_v
        receta.total_materiales = total_m
        receta.save()

        return receta

#pylint: disable=no-member
from rest_framework import serializers
from .models import Receta, MaterialReceta#, VariedadFlorReceta
from apps.materiales.models import Material
from apps.materiales.serializers import MaterialSerializer
#from apps.variedadFlor.models import VariedadFlor

"""
class VariedadFlorRecetaSerializer(serializers.ModelSerializer):
    variedad = serializers.CharField()

    class Meta:
        model = VariedadFlorReceta
        fields = "__all__"
    
    def create(self, validated_data):
        variedad_name = validated_data.pop("variedad")

        try:
            variedad_obj = VariedadFlor.objects.get(name=variedad_name)
        except VariedadFlor.DoesNotExist as exc:
            raise serializers.ValidationError({
                "error": "el material ingresado no existe"
            }) from exc
        
        cant_tallos_por_ramo = validated_data.get("quantity_stems")
        cant_ramos = validated_data.get("quantity_bouquets")
        cant_total_tallos = cant_tallos_por_ramo * cant_ramos
        precio_total_ = """


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
    detalles_material = MaterialRecetaSerializer(many=True, write_only=True) # lista de los materiales
    materiales = MaterialRecetaReadSerializer(source="materialreceta_set", many=True, read_only=True)

    class Meta:
        model = Receta
        fields = ["num_receta", "detalles_material", "materiales", "total_materiales"]

    def create(self, validated_data):
        detalles = validated_data.pop("detalles_material")
        receta = Receta.objects.create(**validated_data)

        total = 0

        for i in detalles:
            material = i["material"]
            quantity = i["quantity"]

            precio_total = material.price * quantity
            total += precio_total

            MaterialReceta.objects.create(
                material = material,
                receta = receta,
                quantity = quantity,
                price_total = precio_total
            )

        receta.total_materiales = total
        receta.save()

        return receta

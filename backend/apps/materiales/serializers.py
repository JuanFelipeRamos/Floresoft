#pylint: disable=no-member
from rest_framework import serializers
from .models import CategoriaMaterial, Material

class CategoriaMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMaterial
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField()

    class Meta:
        model = Material
        fields = "__all__"

    def create(self, validated_data):
        name_categoria = validated_data.pop("categoria")

        try:
            categ_obj = CategoriaMaterial.objects.get(name= name_categoria)
        except CategoriaMaterial.DoesNotExist as exc:
            raise serializers.ValidationError({
                "error": "la categoria ingresada no existe"
            }) from exc

        material = Material.objects.create(
            categoria = categ_obj,
            **validated_data
        )

        return material

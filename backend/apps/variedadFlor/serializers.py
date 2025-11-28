#pylint: disable=no-member
from rest_framework import serializers
from .models import TypeVariedadFlor, VariedadFlor

class TypeVariedadFlorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeVariedadFlor
        fields = "__all__"


class VariedadFlorSerializer(serializers.ModelSerializer):
    type_flor = serializers.CharField()

    class Meta:
        model = VariedadFlor
        fields = "__all__"

    def create(self, validated_data):
        type_name = validated_data.pop("type_flor")

        try:
            type_obj = TypeVariedadFlor.objects.get(name=type_name)
        except TypeVariedadFlor.DoesNotExist as exc:
            raise serializers.ValidationError({
                "error": "el tipo de variedad ingresado no existe"
            }) from exc

        variedad = VariedadFlor.objects.create(
            type_flor = type_obj,
            **validated_data
        )

        return variedad

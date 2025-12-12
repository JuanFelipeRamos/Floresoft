#pylint: disable=no-member
from rest_framework import serializers
from .models import Receta, VariedadFlorReceta, MaterialReceta, ManoDeObraReceta
from apps.variedadFlor.models import VariedadFlor
from apps.variedadFlor.serializers import VariedadFlorSerializer
from apps.materiales.models import Material
from apps.materiales.serializers import MaterialSerializer
from apps.manoDeObra.models import ManoDeObra, CostoVariedadTinturar
from apps.manoDeObra.serializers import ManoDeObraSerializer

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
        fields = ["id", "variedad", "quantity_stems_of_variety", "style_stems", "price_total_tallos"]


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


class ManoDeObraRecetaSerializer(serializers.Serializer):
    mano_de_obra = serializers.CharField()

    class Meta:
        model = ManoDeObraReceta
        fields = "__all__"

    def validate_mano_de_obra(self, value):
        try:
            mano_de_obra = ManoDeObra.objects.get(name=value)
        except ManoDeObra.DoesNotExist as exc:
            raise serializers.ValidationError({
                "error": "la mano de obra ingresada no existe"
            }) from exc

        return mano_de_obra


# serializer para listar las manos de obra con detalles en la lista de manos de obra de una receta
class ManoDeObraRecetaReadSerializer(serializers.ModelSerializer):
    material = ManoDeObraSerializer(read_only=True)
    class Meta:
        model = ManoDeObraReceta
        fields = ["id", "mano_de_obra", "price_total"]


class RecetaSerializer(serializers.ModelSerializer):
    detalles_variedad = VariedadFlorRecetaSerializer(
            many=True,
            write_only=True
        ) # lista de variedades de la receta

    variedades = VariedadFlorRecetaReadSerializer(
            source="variedadflorreceta_set",
            many=True,
            read_only=True
        )

    detalles_material = MaterialRecetaSerializer(
            many=True,
            write_only=True
        ) # lista de materiales de la receta

    materiales = MaterialRecetaReadSerializer(
            source="materialreceta_set",
            many=True,
            read_only=True
        )

    detalles_mano_obra = ManoDeObraRecetaSerializer(
            many=True,
            write_only=True
        ) # Lista de manos de obra de la receta

    manos_de_obra = ManoDeObraRecetaReadSerializer(
            source="manodeobrareceta_set",
            many=True,
            read_only=True
        )

    class Meta:
        model = Receta
        fields = [
            "num_receta",
            "quantity_bouquets",
            "quantity_stems_for_bouquets",

            "detalles_variedad",
            "variedades",
            "total_variedades",

            "detalles_material",
            "materiales",
            "total_materiales",

            "detalles_mano_obra",
            "manos_de_obra",
            "total_mano_de_obra"
            ]

    def create(self, validated_data):
        detalles_v = validated_data.pop("detalles_variedad")
        detalles_m = validated_data.pop("detalles_material")
        detalles_o = validated_data.pop("detalles_mano_obra")
        receta = Receta.objects.create(**validated_data)

        total_v = 0
        total_m = 0
        total_o = 0

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

        # recorrer lista de manos de obra-------------------------------------------------
        for i in detalles_o:
            mano_de_obra = i["mano_de_obra"]

            if mano_de_obra == "Tinturado":
                variedades_receta = detalles_v
                variedades_para_tinturar = [
                    item for item in variedades_receta
                    if item["style_stems"] == "Tinturado"
                ]

                for variedad in variedades_para_tinturar:
                    nombre = variedad["variedad"]
                    variedad_tint = CostoVariedadTinturar.objects.get(name_variedad=nombre)
                    costo_variedad_tint = variedad_tint.price
                    cantidad_variedades_tint = variedades_para_tinturar.len()
                    # multiplicar el costo de tinturar ese tallo por la cantidad de tallos a tinturar

            ManoDeObraReceta.objects.create(
                mano_de_obra = mano_de_obra,
                receta = receta,
                price_total = x
                # ver cómo obtener la variedad que necesita la mano de obra
                # (ARMADO, ENCAPUCHADO PARA TODOS LOS TALLOS)
                # TINTURADO SOLO PARA ALGUNOS
            )

        receta.total_variedades = total_v
        receta.total_materiales = total_m
        receta.save()

        return receta

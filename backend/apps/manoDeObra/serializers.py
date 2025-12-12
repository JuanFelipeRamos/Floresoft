from rest_framework import serializers
from .models import ManoDeObra, CostoVariedadTinturar

class ManoDeObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManoDeObra
        fields = "__all__"


class CostoVariedadTinturarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostoVariedadTinturar
        fields = "__all__"

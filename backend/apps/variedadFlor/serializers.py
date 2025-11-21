from rest_framework import serializers
from .models import TypeVariedadFlor, VariedadFlor

class TypeVariedadFlorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeVariedadFlor
        fields = "__all__"


class VariedadFlorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariedadFlor
        fields = "__all__"

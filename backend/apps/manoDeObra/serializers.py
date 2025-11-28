from rest_framework import serializers
from .models import ManoDeObra

class ManoDeObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManoDeObra
        fields = "__all__"

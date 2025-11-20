from rest_framework import serializers
from .models import UsuarioAdministrador

class UsuarioAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAdministrador
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        pwd = validated_data.pop("password")
        user = UsuarioAdministrador(**validated_data)
        user.set_password(pwd)
        user.save()
        return user

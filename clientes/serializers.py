from clientes.models import Cliente
from loja.models import CATEGORIAS
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        extra_kwargs = {'password': {'write_only': True}}
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'password'
        )

    def create(self, validated_data):
        user = super(ClienteSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



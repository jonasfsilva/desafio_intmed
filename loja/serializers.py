from loja.models import Produto
from loja.models import Pedido
from rest_framework import serializers


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = (
            'id',
            'nome',
            'descricao',
            'valor',
            'categoria'
        )


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = (
            'id',
            'produtos',
            'status',
            'data_realizacao',
        )
from loja.models import Produto
from loja.models import Pedido
from loja.models import CATEGORIAS
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
    
    def validate_produtos(self, attrs):
        msg = 'É necessesario escolher no minimo um produto de cada categoria'
        
        produtos = attrs
        if len(produtos) < len(CATEGORIAS):
            raise serializers.ValidationError(msg)
        
        categorias_index = list(dict(CATEGORIAS))
        for p in produtos:
            if not p.categoria in categorias_index:
                raise serializers.ValidationError(msg)

        return attrs

    def validate(self, attrs):
        return attrs
        
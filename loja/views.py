from django.shortcuts import render
from rest_framework import viewsets
from loja.models import Produto
from loja.models import Pedido
from loja.serializers import ProdutoSerializer
from loja.serializers import PedidoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
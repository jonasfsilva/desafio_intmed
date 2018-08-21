from django.shortcuts import render
from rest_framework import viewsets
from loja.models import Produto
from loja.models import Pedido
from loja.serializers import ProdutoSerializer
from loja.serializers import PedidoSerializer
from loja.permissions import IsAdmin
from rest_framework import status
from rest_framework.response import Response


class ProdutoViewSet(viewsets.ModelViewSet):
    
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (IsAdmin,)


class PedidoViewSet(viewsets.ModelViewSet):
    
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_queryset(self):
        """ 
            O cliente logado consegue ver apenas seus pedidos, 
            enquanto o administrador vê de todos os clientes.
        """
        user = self.request.user
        if not user.is_staff:
            return self.queryset.filter(cliente=user)
        return self.queryset

    def perform_create(self, serializer):
        # serializer.save(usuario=self.request.user)
        serializer.save()
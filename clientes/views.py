from django.shortcuts import render
from rest_framework import viewsets
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from rest_framework.permissions import AllowAny


class ClienteViewSet(viewsets.ModelViewSet):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        """ 
            O (cliente) logado consegue ver apenas a 
            seu proprio perfil, enquanto o administrador 
            vê de todos os clientes.
        """
        user = self.request.user
        if not user.is_staff:
            return self.queryset.filter(pk=user.pk)
        return self.queryset
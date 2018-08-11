from django.shortcuts import render
from rest_framework import viewsets
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from rest_framework.permissions import AllowAny


class ClienteViewSet(viewsets.ModelViewSet):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (AllowAny, )

""" Comando para popular o banco """
import os
from django.core.management import BaseCommand, call_command
from django.core.management import CommandParser
from loja.models import Produto
from loja.models import Pedido
from loja.models import CATEGORIAS
from clientes.models import Cliente


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        self.create_produtos()
        self.create_clientes()
        self.create_pedidos()
            
    def create_clientes(self):
        pass

    def create_pedidos(self):
        pass
        
    def create_produtos(self):
        categorias = dict(CATEGORIAS).keys()
        produtos = Produto.objects.all()

        if len(produtos) < len(categorias):
            for c in categorias:
                data = {
                    'nome': 'Peça {0}'.format(c),
                    'descricao': '-',
                    'valor': 100.00,
                    'categoria': c
                }
                produto = Produto.objects.create(**data)
                print(produto)
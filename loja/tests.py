import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from clientes.models import Cliente
from loja.models import Pedido
from loja.models import Produto
from loja.models import CATEGORIAS
from rest_framework.authtoken.models import Token
from autenticacao.models import User


class PedidoApiTestCase(TestCase):
    
    def setUp(self):
        user_data = {
            'email':'admin@gmail.com',
            'name':'test',
            'phone':'test',
        }
        self.user = User.objects.create(**user_data)
        self.user.set_password('admin')
        self.user.save()
        self.api_client = APIClient()
        self.api_client.force_authenticate(user=self.user)

    
    def test_can_create_pedido(self):
        cliente_data = {
            'email':'cliente@gmail.com',
            'name':'test',
            'phone':'test',
        }
        cliente = Cliente.objects.create(**cliente_data)
        produtos = []
        for c in list(dict(CATEGORIAS)):
            p = Produto(nome='Processador Celeron', 
                categoria=c, valor=150)
            p.save()
            produtos.append(p.pk)

        data = {
            'status':1,
            'produtos':produtos,
            'cliente':cliente.pk
        }

        response = self.api_client.post('/api/pedidos/', data)
        content = json.loads(response.content.decode('utf8'))
        self.assertTrue(Pedido.objects.count())


    def test_can_create_pedido_to_user_request(self):
        cliente_data = {
            'name':'test',
            'phone':'test',
            'email':'cliente@gmail.com',
        }
        cliente = Cliente.objects.create(**cliente_data)
        produtos = []
        for c in list(dict(CATEGORIAS)):
            p = Produto(nome='Processador Celeron', 
                categoria=c, valor=150)
            p.save()
            produtos.append(p.pk)

        data = {
            'status':1,
            'produtos':produtos,
            'cliente':cliente.pk
        }

        response = self.api_client.post('/api/pedidos/', data)
        content = json.loads(response.content.decode('utf8'))
        self.assertEqual(Pedido.objects.first().cliente.pk, cliente.pk)
        self.assertTrue(Pedido.objects.count())

    
    def test_cant_create_pedido_whithout_all_categories_in_products(self):
        produtos = []
        p = Produto(nome='Peça', 
            categoria=1, valor=150)
        p.save()

        data = {
            'status':1,
            'produtos':[p.pk]
        }

        response = self.api_client.post('/api/pedidos/', data)
        content = json.loads(response.content.decode('utf8'))

        self.assertEqual(content.get('produtos')[0], 'É necessesario escolher no minimo um produto de cada categoria')
        self.assertFalse(Pedido.objects.count())
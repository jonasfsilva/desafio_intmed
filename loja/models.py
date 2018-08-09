from django.db import models


CATEGORIAS = (
    ( 1, 'Processadores')
    ( 2, 'Memória RAM'),
    ( 3, 'Disco Rígido/SSD'),
    ( 4, 'Placa de Vídeo'),
    ( 5, 'Gabinete'),
    ( 6, 'Placa mãe'),
    ( 7, 'Fonte'),
)

STATUS_PEDIDO = (
    (1,'Pedido Realizado'),
    (2,'Separação em estoque'),
    (3,'Em montagem'),
    (4,'Realização de testes'),
    (5,'Concluído'),
)


class Produto(models.Model):
    
    categoria = models.PositiveIntegerField(choices=CATEGORIAS, default=1)
    nome = models.CharField(max_length=40)
    descricao = models.TextField()
    valor = models.DecimalField()


class Pedido(models.Model):
    
    produtos = models.ManyToManyField(Produto)
    status = models.PositiveIntegerField(choices=STATUS_PEDIDO)
    data_realizacao = models.DateTimeField(auto_now_add=True)


class ProdutoEstoque(models.Model):

    produto = models.OneToOneField(Produto)
    quantidade = models.PositiveIntegerField(default=1)    

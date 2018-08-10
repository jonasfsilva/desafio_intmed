from django.db import models
from django.contrib.auth.models import User


CATEGORIAS = (
    ( 1, 'Processadores'),
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
    descricao = models.TextField(null=True, blank=True)
    valor = models.DecimalField(decimal_places=2, max_digits=5)


class Pedido(models.Model):
    
    produtos = models.ManyToManyField(Produto)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.PositiveIntegerField(choices=STATUS_PEDIDO)
    data_realizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}|{1}".format(self.status, self.data_realizacao)
    
    def save(self, *args, **kwargs):
        super(Pedido, self).save(*args, **kwargs)


class ProdutoEstoque(models.Model):

    produto = models.OneToOneField(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)    

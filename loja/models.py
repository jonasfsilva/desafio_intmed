from django.db import models
from autenticacao.models import User
from clientes.models import Cliente
from django.db.models import Sum


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

    def __str__(self):
        return "{0} R$: {1} | Categoria: ({2})".format(
            self.nome, 
            self.valor, 
            dict(CATEGORIAS).get(self.categoria)
        )


class Pedido(models.Model):
    
    produtos = models.ManyToManyField(Produto)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    status = models.PositiveIntegerField(choices=STATUS_PEDIDO)
    data_realizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cliente: {0}|{1}".format(
            self.cliente, self.status)
    
    def get_valor_total(self):
        valor_result = self.produtos.all().aggregate(
            valor=Sum('valor'))
        return valor_result.get('valor', 0.0)
    
    def save(self, *args, **kwargs):
        super(Pedido, self).save(*args, **kwargs)


class ProdutoEstoque(models.Model):

    produto = models.OneToOneField(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)    

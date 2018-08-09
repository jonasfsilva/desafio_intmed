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


class Produto(models.Model):
    
    # categoria
    # nome
    # descricao
    # valor
    pass


class Estoque(models.Model):

    # produto = 
    # quantidade =     


STATUS_PEDIDO = (
    (1,'Pedido Realizado'),
    (2,'Separação em estoque'),
    (3,'Em montagem'),
    (4,'Realização de testes'),
    (5,'Concluído'),
)
class Pedido(models.Model):
    
    # produtos = 
    # status = 
    pass

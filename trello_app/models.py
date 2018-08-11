# from django.db import models
# from loja.models import Pedido


# class Board(models.Model):
    
#     trello_id = models.CharField(max_length=200)
#     nome = models.CharField(max_length=100)


# class List(models.Model):
    
#     trello_id = models.CharField(max_length=200)
#     nome = models.CharField(max_length=100)
#     board = models.ForeignKey(Board, on_delete=models.PROTECT)


# class Card(models.Model):

#     trello_id = models.CharField(max_length=200)
#     nome = models.CharField(max_length=100)
#     board = models.ForeignKey(List, on_delete=models.PROTECT)


# class CardPedido(models.Model):

#     card = models.OneToOneField(Card, on_delete=models.CASCADE)
#     pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)

#     # Criar este elemento ao receber um pedido
#     # e confirmar o save dos many to many

#     # Ao receber a atualizacao de um webhook
#     # Alterar o status do pedido, deste card no post_save

from django.db import models
from loja.models import Pedido
from jsonfield import JSONField


# class Board(models.Model):
    
#     trello_id = models.CharField(max_length=200)
#     nome = models.CharField(max_length=100)


# class List(models.Model):
    
#     trello_id = models.CharField(max_length=200)
#     nome = models.CharField(max_length=100)
#     board = models.ForeignKey(Board, on_delete=models.PROTECT)


class WebHookReceived(models.Model):
    
    data = JSONField()
    data_recebimento = models.DateTimeField(auto_now_add=True)

    # TODO
        # - Receber Hook
        # - Pegar o id_model
        # - Filtrar para pegar o card do pedido com o id
            # - CardPedido.objects.filter(card__trello_id=id_model)
        # - Verificar a coluna do card
        # - Alterar o Status do Pedido


class Card(models.Model):

    trello_id = models.CharField(max_length=200)

    def __str__(self):
        return self.trello_id


class CardPedido(models.Model):

    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}:{1}".format(self.card.trello_id, self.pedido.status)
from django.db.models.signals import post_save
from django.dispatch import receiver
from trello_app.trello import TrelloExternalApi
from django.conf import settings


def atualizar_pedidos(sender, instance, **kwargs):
    """ Faz a adição de card no trello apos a adição. """

    action = kwargs.get('action')
    if action == 'post_add':
        trello = TrelloExternalApi()
        board = trello.get_default_board()
        name = "{0} {1}".format("Pedido", instance.id)
        card = trello.add_card_to_board(instance.status, name)
        print('despois de adicionar', card)
    
    

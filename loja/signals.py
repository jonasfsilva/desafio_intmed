from django.db.models.signals import post_save
from django.dispatch import receiver
from trello_app.trello import TrelloExternalApi
from django.conf import settings
from trello_app.models import Card
from trello_app.models import CardPedido


def atualizar_pedidos(sender, instance, **kwargs):
    """ Faz a adição de card no trello apos a adição. """

    # Cliente nome email telefone
    # Componentes Nomes

    action = kwargs.get('action')
    if action == 'post_add':
        trello = TrelloExternalApi()
        board = trello.get_default_board()
        name = "{0} {1}".format("Pedido", instance.id)
        card = trello.add_card_to_board(instance.status, name)

        card_obj = Card.objects.create(trello_id=card.id)
        card_pedido_obj = CardPedido.objects.create(card=card_obj, pedido=instance)
        
        trello.make_card_description(card, instance)
        print('despois de adicionar', card)
    
    

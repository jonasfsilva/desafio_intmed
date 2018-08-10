from django.db.models.signals import post_save
from django.dispatch import receiver


def atualizar_pedidos(sender, instance, **kwargs):
    # TODO adicionar mudança de status do quadro
    action = kwargs.get('action')
    if action == 'post_add':
        print('despois de adicionar')
        # ATUALIZAR TRELLO
            # - Pegar lista 
            # - Adicionar Pedido
        pass
    
    

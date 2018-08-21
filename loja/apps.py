from django.apps import AppConfig
# from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class LojaConfig(AppConfig):
    name = 'loja'

    def ready(self):
        from loja.signals import atualizar_pedidos
        from loja.models import Pedido
        m2m_changed.connect(atualizar_pedidos, sender=Pedido.produtos.through)

from django.db import models
from autenticacao.models import User


class ClienteManager(models.Manager):

    def get_queryset(self):
        """ Querys feitas com o model Cliente retornarão 
            Apenas clientes nunca administradores com is_staff=True
        """
        return super().get_queryset().filter(is_staff=False)


class Cliente(User):
    
    class Meta:
        proxy = True

    objects = ClienteManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        """ Poderiam ser utilizados grupos tambem 
            mas optei por usar um proxy com manager customizado.
        """
        self.is_staff = False
        super(Cliente, self).save(*args, **kwargs)

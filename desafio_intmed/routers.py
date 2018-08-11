from rest_framework import routers
from loja.views import ProdutoViewSet
from loja.views import PedidoViewSet
from clientes.views import ClienteViewSet


router = routers.DefaultRouter()

router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'clientes', ClienteViewSet)
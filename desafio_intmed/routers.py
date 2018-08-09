from rest_framework import routers
from loja.views import ProdutoViewSet
from loja.views import PedidoViewSet


router = routers.DefaultRouter()

router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)
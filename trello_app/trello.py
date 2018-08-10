from trello import TrelloClient 
from django.conf import settings

# Pedido Realizado 
# Separação em estoque 
# Em montagem 
# Realização de testes 
# Concluído 

# TODO criar classe e criar metodos

client = TrelloClient(                    
    api_key=settings.TRELLO_KEY,
    token=settings.TRELLO_TOKEN,
)

board = client.get_board(settings.TRELLO_KEY)

board.all_lists()



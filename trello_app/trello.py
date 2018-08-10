from trello import TrelloClient 
from django.conf import settings

# settings.TRELLO_KEY
# Pedido Realizado 
# Separação em estoque 
# Em montagem 
# Realização de testes 
# Concluído 

# TODO criar classe e criar metodos

class TrelloExternalApi:
    
    def __init__(self):
        self.client = TrelloClient(                    
            api_key=settings.TRELLO_KEY,
            token=settings.TRELLO_TOKEN,
        )

    def get_default_board(self):
        board = self.client.get_board(settings.BOARD_ID)
        return board
    
    def get_other_board(self, board_id):
        board = self.client.get_board(board_id)
        return board
    
    def add_card_to_board(self, list_key, card_name):
        board = self.get_default_board()
        board_lists = settings.BOARD_LISTS
        current_list = board.get_list(board_lists.get(
            list_key))
        
        new_card = current_list.add_card(card_name)
        return new_card
        



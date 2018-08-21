from trello import TrelloClient 
from django.conf import settings


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
    
    def make_card_description(self, card, pedido):
        cliente = pedido.cliente
        client_text = """ 
                        \nCliente: 
                        \nNome: {0}
                        \nEmail: {1}
                        \nTelefone: {2}
                      """.format(cliente.name, cliente.email, cliente.phone)

        produtos_names = pedido.produtos.values_list('nome', flat=True)
        descricao_text = "\n".join(produtos_names)
        
        full_text = "{0}\n{1}\n{2}".format(
            client_text, 
            'Componentes:', 
            descricao_text
        )
        card.set_description(full_text)

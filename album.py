from nodo import Nodo


class Album:

    def __init__(self):
        self.inicio = None    # Aponta para a primeira figurinha da lista encadeada.
        self.repetidas = None # Aponta para a primeira figurinha da lista de repetidas.
        self.quantidade = 0   # Conta quantas figurinhas únicas já foram inseridas no álbum.
        self.total_album = 500 # Quantidade total de figurinhas necessárias para completar o álbum.

    def inserir(self, figurinha):
        pass

    def remover(self, id):
        pass

    def consultar(self, id):
        pass

    def ver_album_completo(self):
        pass

    def ver_porcentagem_concluida(self):
        pass
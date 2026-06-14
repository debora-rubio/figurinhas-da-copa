from nodo import Nodo

class Album:

    def __init__(self):
        self.inicio = None    # Aponta para a primeira figurinha da lista encadeada.
        self.repetidas = None # Aponta para a primeira figurinha da lista de repetidas.
        self.quantidade = 0   # Conta quantas figurinhas únicas já foram inseridas no álbum.
        self.total_album = 500 # Quantidade total de figurinhas necessárias para completar o álbum.

    def inserir(self, figurinha):
        pass    # pass significa: vou implementar isso depois.



    def remover(self, id):
        pass



    def consultar(self, id):
        atual = self.inicio

        while atual is not None:

            if atual.dado.id == id:
                return atual.dado

            atual = atual.proximo

        return None



    def ver_album_completo(self):
        pass

 
 
    def ver_porcentagem_concluida(self):
        pass



    def armazenar_repetida(self, figurinha):
        atual = self.repetidas   # Ele começa procurando se aquela figurinha já está na lista de repetidas.

        while atual is not None:

            if atual.dado.id == figurinha.id:
                atual.dado.quantidade += 1                 # Se já estiver, ele faz: quantidade = quantidade + 1.
                print("Figurinha repetida atualizada.")
                return

            atual = atual.proximo

        nova_repetida = Nodo(figurinha)                     # Se ainda não estiver, ele cria um novo nó.
        nova_repetida.dado.quantidade = 1                   # E coloca essa figurinha na lista de repetidas.

        if self.repetidas is None:
            self.repetidas = nova_repetida
        else:
            atual = self.repetidas

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = nova_repetida

        print("Figurinha repetida armazenada.")



    def mostrar_repetidas(self):
        pass



    def contar_repetidas(self):
        pass
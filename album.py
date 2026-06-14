from nodo import Nodo

class Album:

    def __init__(self):
        self.inicio = None    # Aponta para a primeira figurinha da lista encadeada.
        self.repetidas = None # Aponta para a primeira figurinha da lista de repetidas.
        self.quantidade = 0   # Conta quantas figurinhas únicas já foram inseridas no álbum.
        self.total_album = 500 # Quantidade total de figurinhas necessárias para completar o álbum.

    def inserir(self, figurinha):
        figurinha_encontrada = self.consultar(figurinha.id) # O sistema procura por ex. o ID 10 dentro do álbum.

        if figurinha_encontrada is not None:    # Se encontrou, a figurinha já existe no álbum.

            self.armazenar_repetida(figurinha)  # envia para a lista de repetidas.

            print("Figurinha enviada para a lista de repetidas.")

            return

        novo_nodo = Nodo(figurinha)    # Se não encontrou, Cria um nó da lista encadeada.

        if self.inicio is None:

            self.inicio = novo_nodo

        else:

            atual = self.inicio

            while atual.proximo is not None:

                atual = atual.proximo

            atual.proximo = novo_nodo

        self.quantidade += 1

        print("Figurinha inserida no álbum.")



    def remover(self, id):
        pass    # pass significa: vou implementar isso depois.



    def consultar(self, id):
        atual = self.inicio

        while atual is not None:

            if atual.dado.id == id:
                return atual.dado

            atual = atual.proximo

        return None



    def ver_album_completo(self):    

        if self.inicio is None:                      # verifica se o álbum está vazio.
            print("O álbum está vazio.")
            return

        atual = self.inicio                          # começa na primeira figurinha.

        while atual is not None:             # percorre toda a lista encadeada.

            atual.dado.exibir()              # mostra os dados da figurinha.

            print("------------------------")

            atual = atual.proximo             # vai para o próximo nó.

 
 
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
from nodo import Nodo


class Fila:

    def __init__(self):

        self.inicio = None          # Primeira proposta  de troca da fila. 
        self.fim = None             # Última proposta de troca da fila. 
        self.quantidade = 0         # Quantidade de propostas de trocas na fila.

    def enqueue(self, dado):       # enqueue() Coloca uma proposta de troca no final da fila.

        novo_nodo = Nodo(dado)      # criando um novo nó da lista encadeada.

        if self.inicio is None:     # verifica se a fila está vazia.

            self.inicio = novo_nodo  # Primeiro crio um novo nó para armazenar a proposta de troca.
            self.fim = novo_nodo     # Depois verifico se a fila está vazia através de self.inicio.
                                     # Se estiver vazia, esse novo nó será o primeiro e o último elemento da fila.
        else:
                                    # Caso contrário, ele será inserido no final da fila.
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo

        self.quantidade += 1   # O atributo quantidade controla quantas propostas de troca existem na fila.
                               # Quando uma proposta é inserida com enqueue(), a quantidade aumenta em 1.
                               # Quando uma proposta é removida com dequeue(), a quantidade diminui em 1."

                                  

    def dequeue(self):             # dequeue() Remove a primeira proposta de troca da fila.

        if self.inicio is None:

            print("A fila está vazia.")
            return None

        dado_removido = self.inicio.dado

        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.quantidade -= 1

        return dado_removido
    


    def limpar(self):

        self.inicio = None
        self.fim = None
        self.quantidade = 0







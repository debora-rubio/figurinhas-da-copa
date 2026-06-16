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

        if self.inicio is None:                      # Se não existir nenhuma figurinha, album vazio.                      

            print("O álbum está vazio.")

            return

                                                      # Caso a figurinha esteja logo no início da lista
        if self.inicio.dado.id == id:                 # Remove o primeiro nó.

            self.inicio = self.inicio.proximo

            self.quantidade -= 1

            print("Figurinha removida com sucesso.")

            return

        anterior = self.inicio

        atual = self.inicio.proximo

        while atual is not None:         # percorre a lista nó por nó, procurando a figurinha com o ID especificado.

            if atual.dado.id == id:

                anterior.proximo = atual.proximo

                self.quantidade -= 1                              # Atualiza a quantidade de figurinhas.

                print("Figurinha removida com sucesso.")

                return

            anterior = atual

            atual = atual.proximo

        print("Figurinha não encontrada.")
    



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

 
 
    def ver_porcentagem_concluida(self):                                # quantas figurinhas únicas tem no álbum.

        porcentagem = (self.quantidade / self.total_album) * 100        # o total do álbum, que no caso é 500.

        print("Porcentagem concluída do álbum:", porcentagem, "%")     # Exemplo: 50 figurinhas únicas de 500 = 10%

        return porcentagem



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
    
        if self.repetidas is None:                  # Verifica se a lista de figurinhas repetidas está vazia.
            print("Não há figurinhas repetidas.")  
            return

        atual = self.repetidas                      # Começa pela primeira repetida.

        while atual is not None:                # Percorre todas as figurinhas repetidas.

            atual.dado.exibir()                 # Mostra os dados da figurinha repetida.

            print("------------------------")

            atual = atual.proximo                # Vai para o próximo nó..
        


    def contar_repetidas(self):

        contador = 0

        atual = self.repetidas

        while atual is not None:

            contador += atual.dado.quantidade   # contador = contador + atual.dado.quantidade
                                                # contador, é a variável que guarda o total acumulado.
            atual = atual.proximo               # atual é o nó que estamos visitando no momento.
                                                # dado (atributo), é a figurinha armazenada dentro do nó.
        print("Quantidade total de figurinhas repetidas:", contador)

        return contador


    def consultar_repetida(self, id):       # procura uma figurinha específica dentro da lista de repetidas.

        atual = self.repetidas

        while atual is not None:

            if atual.dado.id == id:
             return atual.dado

            atual = atual.proximo

        return None
    
    
    
    def diminuir_repetida(self, id):

        if self.repetidas is None:
            print("Não há figurinhas repetidas.")
            return

        if self.repetidas.dado.id == id:

            self.repetidas.dado.quantidade -= 1

            if self.repetidas.dado.quantidade <= 0:
                self.repetidas = self.repetidas.proximo
                print("Repetida removida da lista.")

            else:
                print("Quantidade da repetida diminuída.")

            return

        anterior = self.repetidas
        atual = self.repetidas.proximo

        while atual is not None:

            if atual.dado.id == id:

                atual.dado.quantidade -= 1

                if atual.dado.quantidade <= 0:
                    anterior.proximo = atual.proximo
                    print("Repetida removida da lista.")

                else:
                    print("Quantidade da repetida diminuída.")

                return

            anterior = atual
            atual = atual.proximo

        print("Repetida não encontrada.")


    def buscar_por_nome(self, nome):

        atual = self.inicio
        encontrou = False

        while atual is not None:

            if atual.dado.nome.lower() == nome.lower():
                atual.dado.exibir()
                print("------------------------")
                encontrou = True

            atual = atual.proximo

        if encontrou == False:
            print("Nenhuma figurinha encontrada com esse nome.")
    
    def buscar_por_pais(self, pais):

        atual = self.inicio
        encontrou = False

        while atual is not None:

            if atual.dado.pais.lower() == pais.lower():
                atual.dado.exibir()
                print("------------------------")
                encontrou = True

            atual = atual.proximo

        if encontrou == False:
            print("Nenhuma figurinha encontrada desse país.")

            atual = atual.proximo

        if encontrou == False:
            print("Nenhuma figurinha encontrada desse país.")
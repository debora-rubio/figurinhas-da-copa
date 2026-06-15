class Figurinha:
# utilizando os atributos id, nome, país, posição e raridade conforme especificado.
   
    def __init__(self, id, nome, pais, posicao, raridade):
        self.id = id
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

        # quantidade de cópias da figurinha
        self.quantidade = 1


    def exibir(self):
        print("ID:", self.id)
        print("Nome:", self.nome)
        print("País:", self.pais)
        print("Posição:", self.posicao)
        print("Raridade:", self.raridade)

    def exibir_repetida(self):
        print("ID:", self.id)
        print("Nome:", self.nome)
        print("País:", self.pais)
        print("Posição:", self.posicao)
        print("Raridade:", self.raridade)
        print("Quantidade:", self.quantidade)
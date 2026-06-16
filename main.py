from figurinha import Figurinha
from album import Album
from historico import Historico

album_maria = Album()
album_joao = Album()

historico = Historico()

def escolher_album():

    print("1 - Maria")
    print("2 - João")

    opcao = input("Escolha o álbum: ")

    if opcao == "1":
        return album_maria

    elif opcao == "2":
        return album_joao

    else:
        print("Opção inválida.")
        return None



def mostrar_menu():
    print("\n===== ÁLBUM DE FIGURINHAS DA COPA =====")
    print("1 - Inserir figurinha")
    print("2 - Remover figurinha")
    print("3 - Consultar figurinha")
    print("4 - Ver álbum completo")
    print("5 - Ver porcentagem concluída")
    print("6 - Ver figurinhas repetidas")
    print("7 - Contar figurinhas repetidas")
    print("8 - Buscar por nome do jogador")
    print("9 - Buscar por país/seleção")
    print("10 - Registrar proposta de troca")
    print("11 - Efetuar troca automática")
    print("0 - Sair")




opcao = -1

while opcao != 0:

    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro: digite apenas números.")
        continue

    if opcao == 1:

        album_escolhido = escolher_album()

        if album_escolhido is not None:

            try:
                id = int(input("Digite o ID da figurinha: "))
            except ValueError:
                print("Erro: o ID deve ser um número.")
                continue

            nome = input("Digite o nome do jogador: ")
            pais = input("Digite o país/seleção: ")
            posicao = input("Digite a posição: ")
            raridade = input("Digite a raridade: ")

            figurinha = Figurinha(id, nome, pais, posicao, raridade)

            album_escolhido.inserir(figurinha)

    elif opcao == 2:

        album_escolhido = escolher_album()

        if album_escolhido is not None:

            try:
                id = int(input("Digite o ID da figurinha que deseja remover: "))
            except ValueError:
                print("Erro: o ID deve ser um número.")
                continue

            album_escolhido.remover(id)

    elif opcao == 3:

        album_escolhido = escolher_album()

        if album_escolhido is not None:

            try:
                id = int(input("Digite o ID da figurinha que deseja consultar: "))
            except ValueError:
                print("Erro: o ID deve ser um número.")
                continue

            figurinha = album_escolhido.consultar(id)

            if figurinha is not None:
                figurinha.exibir()
            else:
                print("Figurinha não encontrada.")

    elif opcao == 4:

        album_escolhido = escolher_album()

        if album_escolhido is not None:
            album_escolhido.ver_album_completo()

    elif opcao == 5:

        album_escolhido = escolher_album()

        if album_escolhido is not None:
            album_escolhido.ver_porcentagem_concluida()

    elif opcao == 6:

        album_escolhido = escolher_album()

        if album_escolhido is not None:
            album_escolhido.mostrar_repetidas()

    elif opcao == 7:

        album_escolhido = escolher_album()

        if album_escolhido is not None:
            album_escolhido.contar_repetidas()

    elif opcao == 8:

        album_escolhido = escolher_album()

        if album_escolhido is not None:

            nome = input("Digite o nome do jogador: ")

            album_escolhido.buscar_por_nome(nome)

    elif opcao == 9:

        album_escolhido = escolher_album()

        if album_escolhido is not None:

            pais = input("Digite o país/seleção: ")

            album_escolhido.buscar_por_pais(pais)

    elif opcao == 10:

        try:
            id_maria = int(input("Digite o ID da repetida da Maria: "))
            id_joao = int(input("Digite o ID da repetida do João: "))
        except ValueError:
            print("Erro: os IDs devem ser números.")
            continue

        historico.registrar_proposta("Maria", id_maria, "João", id_joao)

    elif opcao == 11:

        historico.efetuar_troca_automatica(album_maria, album_joao)

    elif opcao == 0:

        print("Encerrando o sistema...")

    else:

        print("Opção inválida.")





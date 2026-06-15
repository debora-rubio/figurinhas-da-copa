from figurinha import Figurinha
from album import Album
from historico import Historico


album_principal = Album()
historico = Historico()


def mostrar_menu():
    print("\n===== ÁLBUM DE FIGURINHAS DA COPA =====")
    print("1 - Inserir figurinha")
    print("2 - Remover figurinha")
    print("3 - Consultar figurinha")
    print("4 - Ver álbum completo")
    print("5 - Ver porcentagem concluída")
    print("6 - Ver figurinhas repetidas")
    print("7 - Contar figurinhas repetidas")
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

        album_principal.inserir(figurinha)

    elif opcao == 2:

        try:
            id = int(input("Digite o ID da figurinha que deseja remover: "))
        except ValueError:
            print("Erro: o ID deve ser um número.")
            continue

        album_principal.remover(id)

    elif opcao == 3:

        try:
            id = int(input("Digite o ID da figurinha que deseja consultar: "))
        except ValueError:
            print("Erro: o ID deve ser um número.")
            continue

        figurinha = album_principal.consultar(id)

        if figurinha is not None:
            figurinha.exibir()
        else:
            print("Figurinha não encontrada.")

    elif opcao == 4:

        album_principal.ver_album_completo()

    elif opcao == 5:

        album_principal.ver_porcentagem_concluida()

    elif opcao == 6:

        album_principal.mostrar_repetidas()

    elif opcao == 7:

        album_principal.contar_repetidas()

    elif opcao == 0:

        print("Encerrando o sistema...")

    else:

        print("Opção inválida.")
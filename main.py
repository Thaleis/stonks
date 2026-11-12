import options as o
import functions as f

while True:
    opcao = o.inicio_do_sistema()

    if opcao == 1:

        while True:
            o.adicionar_produto()
            if f.validar_resposta("Deseja continuar? [S] [N]: ", ["S", "N"]) == "N":
                break
            print()

    elif opcao == 2:

        while True:
            o.consultar_produto()
            if f.validar_resposta("Deseja continuar? [S] [N]: ", ["S", "N"]) == "N":
                break
            print()

    elif opcao == 3:
        o.listar()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == 4:
        pass

    elif opcao == 5:
        pass

    elif opcao == 6:
        pass

    elif opcao == 7:
        break

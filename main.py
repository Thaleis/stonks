import options as o
import functions as f


def repetir(operacao):
    """Executa a operação até o usuário responder que não deseja continuar."""
    while True:
        operacao()
        if f.validar_resposta("Deseja continuar? [S] [N]: ", ["S", "N"]) == "N":
            break
        print()


def executar_opcao(opcao):
    if opcao == 1:
        repetir(o.adicionar_produto)

    elif opcao == 2:
        repetir(o.consultar_produto)

    elif opcao == 3:
        o.listar()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == 4:
        o.alterar_quantidade()

    elif opcao == 5:
        o.alterar_preco_produto()

    elif opcao == 6:
        o.excluir_produto()


def executar():
    while True:
        opcao = o.inicio_do_sistema()

        if opcao == 7:
            print("Até logo!")
            break

        try:
            executar_opcao(opcao)
        except (KeyboardInterrupt, EOFError):
            raise
        except Exception as erro:
            print(f"\nOcorreu um erro inesperado: {erro}")
            print("A operação foi cancelada. Voltando ao menu...\n")


try:
    executar()
except (KeyboardInterrupt, EOFError):
    print("\nPrograma encerrado pelo usuário.")

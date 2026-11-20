import functions as f


def inicio_do_sistema():
    print("=" * 37)
    print("Stonks - Sistema de Gestão de Estoque")
    print("=" * 37)
    print("""
1. Cadastrar
2. Consultar Produto
3. Listar Produtos
4. Alterar Quant. do Produto
5. Alterar Valor do Produto
6. Excluir Produto
7. Sair
""")
    print("=" * 37)
    opcao = f.ler_inteiro("Selecione uma opção: ", minimo=1, maximo=7)
    print("=" * 37)
    return opcao


def adicionar_produto():
    print("Qual o nome do produto?")
    nome_produto = f.ler_texto("- ").capitalize()

    if f.buscar_produto(f.carregar_produtos(), nome_produto):
        print(f"O produto '{nome_produto}' já está cadastrado!")
        return

    print(f"Qual a quantidade inicial de {nome_produto}? (Enter = 0)")
    qtd_produto = f.ler_inteiro("- ", minimo=0, maximo=f.VALOR_MAXIMO, padrao=0)

    print("Qual o valor unitário desse produto?")
    preco_produto = f.ler_decimal("- ", minimo=0)

    if f.adicionar_ao_arquivo({"nome": nome_produto,
                               "quantidade": qtd_produto,
                               "preço": round(preco_produto, 2)}):
        print(f"Produto '{nome_produto}' cadastrado com sucesso!")


def consultar_produto():
    produtos = f.carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda!")
        return

    print("Qual produto deseja consultar?")
    produto = f.buscar_produto(produtos, f.ler_texto("- "))
    if produto is None:
        print("Produto não encontrado!")
        return

    print("\nProduto encontrado!")
    print(f"Nome: {produto['nome']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Preço: R$ {produto['preço']:.2f}")


def listar():
    produtos = f.carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda!")
        return

    print(f"{'Produto':<20} {'Qtd':>6} {'Preço unit.':>12} {'Total':>12}")
    print("-" * 53)

    valor_estoque = 0
    for produto in produtos:
        total = produto["quantidade"] * produto["preço"]
        valor_estoque += total
        preco_txt = f"R$ {produto['preço']:.2f}"
        total_txt = f"R$ {total:.2f}"
        print(f"{produto['nome']:<20} {produto['quantidade']:>6} "
              f"{preco_txt:>12} {total_txt:>12}")

    print("-" * 53)
    print(f"{len(produtos)} produto(s) | Valor total em estoque: R$ {valor_estoque:.2f}")


def alterar_quantidade():
    produtos = f.carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda!")
        return

    print("Qual produto deseja alterar a quantidade?")
    produto = f.buscar_produto(produtos, f.ler_texto("- "))
    if produto is None:
        print("Produto não encontrado!")
        return

    print(f"Quantidade atual de {produto['nome']}: {produto['quantidade']}")
    print("Nova quantidade")
    produto["quantidade"] = f.ler_inteiro("- ", minimo=0, maximo=f.VALOR_MAXIMO)

    if f.salvar_produtos(produtos):
        print("Quantidade alterada com sucesso!")


def alterar_preco_produto():
    produtos = f.carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda!")
        return

    print("\n=== PRODUTOS DISPONÍVEIS ===")
    f.mostrar_produtos_numerados(produtos)

    print("\nQual produto deseja alterar o valor?")
    produto = f.buscar_produto(produtos, f.ler_texto("- "))
    if produto is None:
        print("Produto não encontrado!")
        return

    print(f"Preço atual de {produto['nome']}: R$ {produto['preço']:.2f}")
    print("Novo valor")
    produto["preço"] = round(f.ler_decimal("- ", minimo=0), 2)

    if f.salvar_produtos(produtos):
        print(f"Valor de '{produto['nome']}' atualizado para R$ {produto['preço']:.2f}.")


def excluir_produto():
    produtos = f.carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda!")
        return

    print("\n=== EXCLUIR PRODUTO ===")
    f.mostrar_produtos_numerados(produtos)

    escolha = f.ler_inteiro("\nNúmero do produto a excluir (Enter = cancelar): ",
                            minimo=1, maximo=len(produtos), padrao=0)
    if escolha == 0:
        print("Exclusão cancelada.")
        return

    produto = produtos[escolha - 1]
    confirmar = f.validar_resposta(
        f"Confirma a exclusão de '{produto['nome']}'? [S] [N]: ", ["S", "N"])
    if confirmar == "N":
        print("Exclusão cancelada.")
        return

    produtos.pop(escolha - 1)
    if f.salvar_produtos(produtos):
        print(f"Produto '{produto['nome']}' excluído com sucesso!")

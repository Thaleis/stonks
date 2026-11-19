import functions as f
import ast


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

    print(f"Qual a quantidade inicial de {nome_produto}? (Enter = 0)")
    qtd_produto = f.ler_inteiro("- ", minimo=0, padrao=0)

    print("Qual o valor unitário desse produto?")
    preco_produto = f.ler_decimal("- ", minimo=0)

    produto = {"nome": nome_produto,
               "quantidade": qtd_produto,
               "preço": preco_produto}

    with open("produtos.txt", "a", encoding="utf-8") as lista:
        lista.write(f"{produto}\n")


def consultar_produto():
    print("Qual produto deseja consultar?")
    nome = f.ler_texto("- ")

    produtos = f.carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda!")
        return

    encontrado = False
    for produto in produtos:
        if str(produto.get("nome", "")).lower() == nome.lower():
            preco = produto.get("preço", produto.get("preco", 0.0))
            print("\nProduto encontrado!")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto.get('quantidade', 0)}")
            print(f"Preço: R$ {preco:.2f}")
            encontrado = True

    if not encontrado:
        print("Produto não encontrado!")


def listar():
    produtos = f.carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda!")
        return

    print(f"{'Produto':<20} {'Qtd':>6} {'Preço unit.':>12} {'Total':>12}")
    print("-" * 53)

    valor_estoque = 0
    for produto in produtos:
        nome = produto.get("nome", "")
        qtd = produto.get("quantidade", 0)
        preco = produto.get("preço", 0.0)
        total = qtd * preco
        valor_estoque += total
        print(
            f"{nome:<20} {qtd:>6} {'R$ ' + f'{preco:.2f}':>12} {'R$ ' + f'{total:.2f}':>12}")

    print("-" * 53)
    print(f"{len(produtos)} produto(s) | Valor total em estoque: R$ {valor_estoque:.2f}")


def alterarquantidade():
    produtos = f.carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado ainda!")
        return
    print("Qual produto deseja alterar a quantidade?")
    nome = f.ler_texto("- ")
    encontrado = False
    for produto in produtos:
        if str(produto.get("nome", "")).lower() == nome.lower():
            produto_encontrado = produto
            encontrado = True
            break
    if not encontrado:

        print("Produto não encontrado...")
        return
    print(
        f"Quantidade atual de {produto_encontrado.get('nome', 0)}: {produto_encontrado.get('quantidade', 0)}")
    print("Nova quantidade")
    nova_qtd = f.ler_inteiro("- ", minimo=0)
    produto_encontrado["quantidade"] = nova_qtd

    with open("produtos.txt", "w", encoding="utf-8") as lista:
        for produto in produtos:
            lista.write(f"{produto} \n")

    print("Quantidade alterada com sucesso!")



def alterar_preco_produto(caminho_arquivo="produtos.txt"):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = [linha.strip() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        print("Ficheiro 'produtos.txt' não encontrado.")
        return

    if not linhas:
        print("Não existem produtos registados.")
        return

    produtos = []
    for linha in linhas:
        try:
            produtos.append(ast.literal_eval(linha))
        except (ValueError, SyntaxError):
            print(f"Linha inválida ignorada em {caminho_arquivo}: {linha}")

    if not produtos:
        print("Nenhum produto válido encontrado.")
        return

    print("\n=== PRODUTOS DISPONÍVEIS ===")
    for indice, produto in enumerate(produtos, start=1):
        print(
            f"{indice} - {produto['nome']} | "
            f"Preço atual: {produto['preço']:.2f} | "
            f"Quantidade: {produto['quantidade']}"
        )

    nome_procurado = input("\nNome do produto para alterar o valor: ").strip().lower()

    for produto in produtos:
        if produto["nome"].strip().lower() == nome_procurado:
            try:
                novo_valor = float(
                    input(f"Novo valor para '{produto['nome']}': ").replace(",", ".")
                )
            except ValueError:
                print("Valor inválido. Introduz um número.")
                return

            if novo_valor < 0:
                print("O valor não pode ser negativo.")
                return

            produto["preço"] = round(novo_valor, 2)

            with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
                for item in produtos:
                    arquivo.write(f"{item}\n")

            print(f"Valor de '{produto['nome']}' atualizado para {produto['preço']:.2f}.")
            return

    print("Produto não encontrado.")

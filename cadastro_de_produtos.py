def adicionar_produto():
    print("Qual o nome do produto?")
    nome_produto = input("- ").strip()
    if not nome_produto:
        print("Digite um nome para o produto")
        return

    print(f"Qual a quantidade inicial de {nome_produto}? ")
    qtd_produto = input("- ")
    if not qtd_produto:
        qtd_produto = 0
    print(f"Qual o valor unitário desse produto?")
    preco_produto = float(input("- ").replace(",", "."))

    produto={"nome": nome_produto,
               "quantidade": int(qtd_produto),
               "preço": preco_produto}
    with open("produtos.txt", "a") as lista:
        lista.write(f"{produto} \n")
    with open('produtos.txt', 'r') as lista_produtos:
        conteudo_produtos=lista_produtos.read()
    print(conteudo_produtos)


for i in range(5):
    adicionar_produto()

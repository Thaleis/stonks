def adicionar_produto():
    print("Qual o nome do produto?")
    nome_produto = input("- ")
    print(f"Qual a quantidade inicial de {nome_produto}? ")
    qtd_produto = input("- ")
    produto = {nome_produto: int(qtd_produto)}
    with open("produtos.txt", "a") as lista:
        lista.write(f"{produto} \n")
    with open('produtos.txt', 'r') as lista_produtos:
        conteudo_produtos = lista_produtos.read()
    print(conteudo_produtos)

for i in range (5):
    adicionar_produto()
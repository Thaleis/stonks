import ast
import math
import os

ARQUIVO_PRODUTOS = "produtos.txt"
VALOR_MAXIMO = 1_000_000_000


def validar_resposta(mensagem, opcoes):
    """Pergunta até a resposta ser uma das opções. Devolve a resposta em maiúsculas.
    Ex.: validar_resposta("Deseja continuar? [S] [N]: ", ["S", "N"])"""
    opcoes = [str(op).upper() for op in opcoes]
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in opcoes:
            return resposta
        print(f"Digite uma opção válida! ({' / '.join(opcoes)})")


def ler_texto(mensagem):
    """Pergunta até receber um texto não vazio."""
    while True:
        resposta = input(mensagem).strip()
        if resposta:
            return resposta
        print("A resposta não pode ficar em branco!")


def ler_inteiro(mensagem, minimo=None, maximo=None, padrao=None):
    """Pergunta até receber um número inteiro dentro do intervalo.
    Se 'padrao' for informado, Enter vazio devolve esse valor."""
    while True:
        resposta = input(mensagem).strip()
        if not resposta and padrao is not None:
            return padrao
        try:
            numero = int(resposta)
        except ValueError:
            print("Digite um número inteiro!")
            continue
        if minimo is not None and numero < minimo:
            print(f"O valor deve ser no mínimo {minimo}!")
        elif maximo is not None and numero > maximo:
            print(f"O valor deve ser no máximo {maximo}!")
        else:
            return numero


def ler_decimal(mensagem, minimo=None, maximo=VALOR_MAXIMO):
    """Pergunta até receber um número decimal (aceita vírgula ou ponto)."""
    while True:
        resposta = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(resposta)
        except ValueError:
            print("Digite um valor numérico! Ex.: 10,50")
            continue

        if not math.isfinite(numero):
            print("Digite um valor numérico! Ex.: 10,50")
        elif minimo is not None and numero < minimo:
            print(f"O valor deve ser no mínimo {minimo}!")
        elif maximo is not None and numero > maximo:
            print(f"O valor deve ser no máximo {maximo}!")
        else:
            return numero


def carregar_produtos():
    """Lê o arquivo de produtos e devolve uma lista de dicionários.
    Linhas vazias ou inválidas são ignoradas. Se o arquivo não existir, devolve []."""
    produtos = []
    ignoradas = 0
    try:
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8", errors="replace") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                try:
                    produto = ast.literal_eval(linha)
                except (ValueError, SyntaxError, TypeError, MemoryError, RecursionError):
                    ignoradas += 1
                    continue
                if not isinstance(produto, dict):
                    ignoradas += 1
                    continue

                nome = str(produto.get("nome", "")).strip()
                quantidade = produto.get("quantidade")
                preco = produto.get("preço", produto.get("preco"))
                if (not nome
                        or not isinstance(quantidade, int) or isinstance(quantidade, bool)
                        or quantidade < 0
                        or not isinstance(preco, (int, float)) or isinstance(preco, bool)
                        or not math.isfinite(preco) or preco < 0):
                    ignoradas += 1
                    continue
                produtos.append({"nome": nome,
                                 "quantidade": quantidade,
                                 "preço": float(preco)})
    except FileNotFoundError:
        pass
    except OSError:
        print(f"Não foi possível ler o arquivo '{ARQUIVO_PRODUTOS}'.")
    if ignoradas:
        print(f"Aviso: {ignoradas} linha(s) inválida(s) em '{ARQUIVO_PRODUTOS}' "
              f"foram ignoradas.")
    return produtos


def salvar_produtos(produtos):
    """Reescreve o arquivo com a lista completa de produtos (um por linha).
    Devolve True se salvou, False se houve erro."""
    temporario = ARQUIVO_PRODUTOS + ".tmp"
    try:
        with open(temporario, "w", encoding="utf-8") as arquivo:
            for produto in produtos:
                arquivo.write(f"{produto}\n")
        os.replace(temporario, ARQUIVO_PRODUTOS)
        return True
    except OSError:
        print(f"Erro ao salvar o arquivo '{ARQUIVO_PRODUTOS}'. Alteração não gravada.")
        return False


def adicionar_ao_arquivo(produto):
    """Acrescenta um único produto ao final do arquivo.
    Devolve True se salvou, False se houve erro."""
    try:
        with open(ARQUIVO_PRODUTOS, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{produto}\n")
        return True
    except OSError:
        print(f"Erro ao salvar o arquivo '{ARQUIVO_PRODUTOS}'. Produto não cadastrado.")
        return False


def buscar_produto(produtos, nome):
    """Procura um produto pelo nome (sem diferenciar maiúsculas/minúsculas).
    Devolve o dicionário do produto ou None se não encontrar."""
    nome = nome.strip().lower()
    for produto in produtos:
        if str(produto["nome"]).strip().lower() == nome:
            return produto
    return None


def mostrar_produtos_numerados(produtos):
    """Mostra os produtos numerados a partir de 1."""
    for indice, produto in enumerate(produtos, start=1):
        print(f"{indice} - {produto['nome']} | "
              f"Preço: R$ {produto['preço']:.2f} | "
              f"Quantidade: {produto['quantidade']}")

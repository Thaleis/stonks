import ast



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


def ler_decimal(mensagem, minimo=None):
    """Pergunta até receber um número decimal (aceita vírgula ou ponto)."""
    while True:
        resposta = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(resposta)
        except ValueError:
            print("Digite um valor numérico! Ex.: 10,50")
            continue
        if minimo is not None and numero < minimo:
            print(f"O valor deve ser no mínimo {minimo}!")
        else:
            return numero






def carregar_produtos():
    produtos = []
    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                try:
                    produto = ast.literal_eval(linha)
                except (ValueError, SyntaxError):
                    continue
                if isinstance(produto, dict):
                    produtos.append(produto)
    except FileNotFoundError:
        pass
    return produtos

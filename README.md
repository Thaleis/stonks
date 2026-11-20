# Stonks – Sistema de Gestão de Estoque

## Descrição do projeto

O **Stonks** é um sistema de controle de estoque desenvolvido em Python e executado
pelo terminal. Ele permite cadastrar, consultar, listar, alterar e excluir produtos,
guardando os dados no arquivo `produtos.txt`. Assim, as informações continuam
disponíveis quando o programa é aberto novamente.

O sistema valida todas as entradas do usuário e trata exceções com `try`/`except`,
para evitar cadastros inconsistentes e impedir que o programa seja encerrado
inesperadamente diante de entradas inválidas.

## Integrantes

- Caue Bertholdi
- Gustavo Gaieski
- Pedro Archer
- Thales Santos

## Instruções para execução

### Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa (usa apenas a biblioteca padrão do Python)

### Passo a passo

1. Baixe ou clone o projeto e abra um terminal na pasta `stonks`.
2. Confira se o Python está instalado:
   ```bash
   python --version
   ```
3. Execute o sistema:
   ```bash
   python main.py
   ```
4. Digite o número da opção desejada no menu e siga as instruções na tela.
5. Para encerrar, escolha a opção **7 – Sair** (ou pressione `Ctrl+C`).

O arquivo `produtos.txt` é criado automaticamente no primeiro cadastro.

## Funcionalidades implementadas

| Opção | Ação | Descrição |
|:-----:|------|-----------|
| 1 | Cadastrar | Cadastra um novo produto (nome, quantidade e preço). Não permite nomes repetidos. |
| 2 | Consultar Produto | Busca um produto pelo nome e mostra seus dados. |
| 3 | Listar Produtos | Mostra todos os produtos em tabela, com o valor total de cada um e do estoque. |
| 4 | Alterar Quant. do Produto | Altera a quantidade em estoque de um produto. |
| 5 | Alterar Valor do Produto | Altera o preço unitário de um produto. |
| 6 | Excluir Produto | Remove um produto escolhido pelo número, com confirmação. |
| 7 | Sair | Encerra o programa. |

A busca por nome não diferencia maiúsculas de minúsculas (`arroz` encontra `Arroz`).
Preços aceitam vírgula ou ponto (`10,50` ou `10.50`).

### Validações e tratamento de erros

- Nome em branco, nome já cadastrado, quantidade ou preço negativos e opções
  fora do menu são recusados, e o sistema pergunta de novo.
- Textos digitados no lugar de números geram uma mensagem de aviso, sem fechar o programa.
- Linhas inválidas no `produtos.txt` são ignoradas na leitura.
- Erros ao ler ou gravar o arquivo são informados ao usuário.
- `Ctrl+C` encerra o sistema com uma mensagem, sem exibir erro.

## Estrutura do projeto

```
stonks/
├── main.py        # Ponto de entrada: mostra o menu e chama a opção escolhida
├── options.py     # Uma função para cada opção do menu
├── functions.py   # Funções auxiliares: leitura/validação de entradas e acesso ao arquivo
└── produtos.txt   # Dados dos produtos (gerado pelo programa, ignorado pelo git)
```

### `functions.py`

| Função | O que faz |
|--------|-----------|
| `validar_resposta(mensagem, opcoes)` | Pergunta até a resposta ser uma das opções (ex.: `S`/`N`). |
| `ler_texto(mensagem)` | Pergunta até receber um texto não vazio. |
| `ler_inteiro(mensagem, minimo, maximo, padrao)` | Lê um inteiro dentro de um intervalo; Enter vazio devolve `padrao`. |
| `ler_decimal(mensagem, minimo)` | Lê um número decimal, aceitando vírgula ou ponto. |
| `carregar_produtos()` | Lê `produtos.txt` e devolve a lista de produtos, ignorando linhas inválidas. |
| `salvar_produtos(produtos)` | Reescreve o arquivo com a lista completa de produtos; trata erros de gravação. |
| `adicionar_ao_arquivo(produto)` | Acrescenta um produto no final do arquivo. |
| `buscar_produto(produtos, nome)` | Procura um produto pelo nome; devolve o produto ou `None`. |
| `mostrar_produtos_numerados(produtos)` | Exibe os produtos numerados a partir de 1. |

### `options.py`

| Função | Opção do menu |
|--------|---------------|
| `inicio_do_sistema()` | Mostra o menu e devolve a opção escolhida (1 a 7). |
| `adicionar_produto()` | 1 – Cadastrar |
| `consultar_produto()` | 2 – Consultar Produto |
| `listar()` | 3 – Listar Produtos |
| `alterar_quantidade()` | 4 – Alterar Quant. do Produto |
| `alterar_preco_produto()` | 5 – Alterar Valor do Produto |
| `excluir_produto()` | 6 – Excluir Produto |

## Formato do arquivo `produtos.txt`

Cada linha guarda um produto como um dicionário Python:

```
{'nome': 'Arroz', 'quantidade': 10, 'preço': 25.9}
{'nome': 'Cafe', 'quantidade': 3, 'preço': 5.0}
```

## Exemplo de uso

```
=====================================
Stonks - Sistema de Gestão de Estoque
=====================================

1. Cadastrar
2. Consultar Produto
3. Listar Produtos
4. Alterar Quant. do Produto
5. Alterar Valor do Produto
6. Excluir Produto
7. Sair

=====================================
Selecione uma opção: 3
=====================================
Produto                 Qtd  Preço unit.        Total
-----------------------------------------------------
Arroz                    10     R$ 25.90    R$ 259.00
Cafe                      3      R$ 5.00     R$ 15.00
-----------------------------------------------------
2 produto(s) | Valor total em estoque: R$ 274.00
```

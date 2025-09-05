import random

# dicionário com direções e incrementos
valor_direcoes = { 
    ("Horizontal", "Normal"):      (0, 1),
    ("Horizontal", "Invertida"):   (0, -1),
    ("Vertical", "Normal"):        (1, 0),
    ("Vertical", "Invertida"):     (-1, 0),
    ("Diagonal Baixo", "Normal"):  (1, 1),
    ("Diagonal Baixo", "Invertida"):(1, -1),
    ("Diagonal Cima", "Normal"):   (-1, 1),
    ("Diagonal Cima", "Invertida"):(-1, -1),
}

 
def verificar_conflitos(palavra, linha, coluna, posicao, direcao, matriz):
    linhas = len(matriz)       # número total de linhas da matriz
    colunas = len(matriz[0])   # número total de colunas da matriz
    delta_linha, delta_coluna = valor_direcoes[(posicao, direcao)] 

    for i, letra in enumerate(palavra): # verifica cada letra da palavra
        nova_linha = linha + i * delta_linha
        nova_coluna = coluna + i * delta_coluna
 
        if not (0 <= nova_linha < linhas and 0 <= nova_coluna < colunas):
            return False # ultrapassou os limites da matriz

        atual = matriz[nova_linha][nova_coluna]
        if atual != 0 and atual != letra:
            return False  # houve conflito de letras
    return True


def inserir_palavra(palavra, linha, coluna, posicao, direcao, jogo):
    delta_linha, delta_coluna = valor_direcoes[(posicao, direcao)] 

    for i, letra in enumerate(palavra): # adiciona cada letra da palavra na matriz
        nova_linha = linha + i * delta_linha
        nova_coluna = coluna + i * delta_coluna
        jogo[nova_linha][nova_coluna] = letra.upper()


def preencher_matriz_aleatoriamente(jogo):
    for i in range(len(jogo)):
        for j in range(len(jogo[0])):
            if jogo[i][j] == 0:
                jogo[i][j] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def verificar_acerto(palavra, linha, coluna, posicao, dicionario):
    palavra_certa = dicionario.get(palavra)
    if palavra_certa != None: # palavra certa
        if (linha - 1) == palavra_certa["linha"] and (coluna - 1) == palavra_certa["coluna"] and posicoes[posicao - 1] == palavra_certa["posicao"]:
            print("\nAcertou!")
            return True
        else: # palavra certa mas alguma informação errada
            print("\nTente novamente, algo estava errado...")
            return False
    else: # palavra não faz parte do jogo
        print("\nA palavra informada não está no caça-palavras")
        return False


def mostrar_jogo(matriz, linhas, colunas):
    linhas = len(matriz)
    colunas = len(matriz[0])

    # Cabeçalho (índices das colunas)
    print("\n    " + " ".join(f"{c + 1:2}" for c in range(colunas)))

    # Separador
    print("   " + "---" * colunas)

    # Cada linha com índice + conteúdo
    for i, linha in enumerate(matriz):
        print(f"{i + 1:2} | " + "  ".join(f"{x}" for x in linha))


lista_palavras = ["Gato", "Cachorro", "Lagarto", "Cobra", "Baleia", "Gorila", "Aguia"] 

# criando matriz do caça palavras
linhas = 10
colunas = 10
jogo = [[0 for _ in range(colunas)] for _ in range(linhas)] # cria lista cheia de zero (colunas) e a replica a lista pela quantidade de linhas
dicionario_controle = {}

posicoes = ["Horizontal", "Vertical", "Diagonal Cima", "Diagonal Baixo"]

# adicionar as palavras na matriz
for palavra in lista_palavras:
    while True:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        posicao = random.choice(posicoes)
        direcao = random.choice(["Normal", "Invertida"])

        if verificar_conflitos(palavra, linha, coluna, posicao, direcao, jogo):
            inserir_palavra(palavra, linha, coluna, posicao, direcao, jogo)
            # cria dicionario com todas as palavras e suas respcetivas informações de localização na matriz
            dicionario_controle[palavra.upper()] = {"linha":linha, "coluna":coluna, "posicao":posicao, "direcao":direcao}
            break

# preencher resto da matriz com letras aleatorias
preencher_matriz_aleatoriamente(jogo)

# começar jogo e buscar palavras corretas
palavras_encontradas = 0
fim_de_jogo = False
while not fim_de_jogo:
    mostrar_jogo(jogo, linhas, colunas)
    print(f"\n{palavras_encontradas} palavras encontradas")

    # obtem respostas do jogador sobre localização e palavra encontrada
    palavra_encontrada = input("\nDigite a palavra que você encontrou: ").strip().upper()
    linha_encontrada = int(input("Digite a linha da primeira letra: "))
    coluna_encontrada = int(input("Digite a coluna da primeira letra: "))
    posicao_encontrada = int(input("Digite a direção (1. Horizontal, 2. Vertical, 3. Diagonal Cima, 4. Diagonal Baixo): "))

    # verifica se a palavra e localização estão corretas
    if verificar_acerto(palavra_encontrada, linha_encontrada, coluna_encontrada, posicao_encontrada, dicionario_controle):
        palavras_encontradas += 1
        if palavras_encontradas == len(lista_palavras): # verifica fim de jogo
            print("\nFim de jogo! Todas as palavras foram encontradas\n")
            fim_de_jogo = True
       






# Jogo da velha NxN
#
# Para armazenar o tabuleiro, é construida uma matriz utilizando listas.
#
# Para verificar se há uma vitória é utilizada a função set(), removendo os
# itens duplicados e, caso uma linha/coluna/diagonal seja composta por apenas
# X ou O (representados por "×" e "◯" para fins de formatação), é declarado um
# vencedor.


winner = ""
x = "×"
o = "◯"
turn = x
table = []


def print_table():
    '''Formata e imprime o tabuleiro.'''
    print()
    divider = "- +"
    for i in range(size):
        divider += " - +"

    header = "  |"
    for i in range(size):
        header += " {} |".format(i + 1)

    print(header)
    print(divider)

    for i in range(size):
        line = "{} |".format(i + 1)
        for j in range(size):
            line += " {} |".format(table[i][j])
        print(line)
        print(divider)

    print()


def check_sequence(sequence):
    '''Recebe uma sequência (lista) e, caso ela seja composta por um caractere único, o retorna.'''
    unique = list(set(sequence))
    if len(unique) == 1 and unique[0] != " ":
        return unique[0]
    return None


def check_win():
    '''Percorre todas as linhas, colunas, e diagonais, verificando se há uma sequência de caracteres (vitória).'''
    for i in range(size):

        row = table[i]
        result = check_sequence(row)
        if result:
            return result

        column = [table[j][i] for j in range(size)]
        result = check_sequence(column)
        if result:
            return result

    diagonal_1 = [table[i][i] for i in range(size)]
    result = check_sequence(diagonal_1)
    if result:
        return result

    diagonal_2 = [table[i][size - 1 - i] for i in range(size)]
    result = check_sequence(diagonal_2)
    if result:
        return result

    return ""


print()
print("Jogo da velha NxN")
print()

size = int(input("➡️  Escolha o tamanho do tabuleiro: "))
for i in range(size):
    row = []
    for j in range(size):
        row.append(" ")
    table.append(row)

while winner == "":
    print_table()
    coords = input("➡️  Jogador {}, escolha as coordenadas (linha,coluna): "
                   .format(turn)).split(",")
    table[int(coords[0]) - 1][int(coords[1]) - 1] = turn
    winner = check_win()
    turn = x if turn == o else o

print_table()
print("Jogador {} ganhou! 🥳".format(winner))
print()

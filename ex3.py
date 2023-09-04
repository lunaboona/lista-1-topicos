# term.ooo
#
# Após ler o arquivo, são filtradas apenas palavras de 5 letras, removidos os
# acentos, e escolhida uma palavra utilizando a biblioteca random.
#
# Evitei utilizar bibliotecas desnecessariamente, então a formatação é feita
# com códigos de cor, e a remoção de acentos com uma função simples utilizando
# um dicionário para mapear as letras com e sem acento.
#
# Enquanto o usuário tem tentativas disponíveis, o jogo pede que ele digite uma
# palavra, validando suas letras e pintando-as para indicar ao usuário o quão
# próximo está da solução.
#
# O jogo também mostra ao usuário as letras já utilizadas que não estão na
# palavra.

import random


class colors:
    BLACK = "\033[1;30m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    GREEN_BOLD = "\033[1;32m"
    YELLOW_BOLD = "\033[1;33m"
    BLUE_BOLD = "\033[1;34m"
    RESET = "\033[0;0m"


def remove_diacritics(word):
    '''Substitui letras com acento por letras sem acento.'''
    map_diacritics = {
        "À": "A",
        "Á": "A",
        "Â": "A",
        "Ã": "A",
        "É": "E",
        "Ê": "E",
        "Í": "I",
        "Ó": "O",
        "Ô": "O",
        "Õ": "O",
        "Ú": "U",
        "Ç": "C",
    }

    result = ""
    for letter in word:
        if letter in map_diacritics:
            result += map_diacritics[letter]
        else:
            result += letter

    return result


def format_available_letters(used):
    '''Formata as letras disponíveis.'''
    str = ""
    all_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                   "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for letter in all_letters:
        str += f"{colors.BLUE_BOLD}{letter}{colors.RESET} " if letter not in used else f"{colors.BLACK}{letter}{colors.RESET} "

    return str


def normalize_guess(guess):
    '''Formata a tentativa para remover espaços e deixar as letras maiúsculas'''
    return guess.strip().upper()


def validate_guess(guess, word):
    '''Valida a tentativa e categoriza as letras entre verde, ama'''
    result = ""
    used = []
    for i, letter in enumerate(guess):
        if letter == word[i]:
            result += f"{colors.GREEN_BOLD}{letter}{colors.RESET}"
        elif letter in word:
            result += f"{colors.YELLOW_BOLD}{letter}{colors.RESET}"
        else:
            result += f"{colors.BLACK}{letter}{colors.RESET}"
            used.append(letter)
    return result, used


def print_game(guesses, used_letters, correct_word=""):
    '''Imprime o "tabuleiro" do jogo.'''
    print()
    print("╭────────────────────── termooo ──────────────────────╮")
    print("│                                                     │")
    if len(guesses) == 0:
        print("├─ instruções ────────────────────────────────────────┤")
        print("│ · digite uma palavra com 5 letras                   │")
        print(
            f"│ · {colors.GREEN}verde{colors.RESET} indica que a letra está no lugar correto    │")
        print(
            f"│ · {colors.YELLOW}amarelo{colors.RESET} indica que a letra está na palavra, mas   │")
        print(f"│   não no lugar correto                              │")
        print(
            f"│ · {colors.BLACK}cinza{colors.RESET} indica que a letra não está na palavra      │")
        print("├─────────────────────────────────────────────────────┤")
        print("│                                                     │")
    else:
        print(
            *[f"│                        {guess}                        │" for guess in guesses], sep="\n")
    if correct_word == "":
        print("│                        _____                        │")
        print("│                                                     │")
        print("├─ letras disponíveis ────────────────────────────────┤")
        print(f"│ {format_available_letters(used_letters)}│")
    else:
        print("│                                                     │")
        print(
            f"│  a palavra correta era {colors.BLUE_BOLD}{correct_word}{colors.RESET}... tente novamente :)  │")
        print("│                                                     │")
    print("╰─────────────────────────────────────────────────────╯")
    print()


def get_words(filename):
    '''Abre o arquivo e carrega as palavras, filtrando por palavras com 5 caracteres e removendo acentos.'''
    with open(filename) as file:
        all_words = [line.strip() for line in file]
    result = []
    for word in all_words:
        if len(word) == 5:
            result.append(remove_diacritics(word).upper())
    return result


turns = 6
win = False
words = get_words("lista_palavras.txt")
word = random.choice(words)
used_letters = []
guesses = []

while turns > 0 and not win:
    print_game(guesses, used_letters)

    guess = ""
    while len(guess) != 5:
        guess = normalize_guess(input("➡️  Digite uma palavra (5 letras): "))

    win = guess == word
    guess, used = validate_guess(guess, word)
    guesses.append(guess)
    used_letters = used_letters + (list(set(used) - set(used_letters)))
    turns -= 1


print_game(guesses, used_letters, word)

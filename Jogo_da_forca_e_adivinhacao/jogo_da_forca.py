import random


def jogar_forca():
    vinheta()
    palavra_secreta = carrega_palavra_secreta()
    inicia_interface(palavra_secreta)

    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_chutadas = []
    perdeu = False
    ganhou = False
    erros = 0

    while (not perdeu) and (not ganhou):
        letra_digitada = verifica_letra_digitada(letras_chutadas)

        if (letra_digitada in palavra_secreta):
            acertou_uma_letra(palavra_secreta, letra_digitada, letras_acertadas)
        else:
            erros += 1

        atualiza_interface(letras_acertadas, erros)

        perdeu = erros == 6
        ganhou = "_" not in letras_acertadas

    if perdeu:
        print("a palavra secreta era {}".format(palavra_secreta))
        print("Você se enforcou e perdeu o jogo. Tente novamente.")
    else:
        print("Parabéns, você venceu!")


def acertou_uma_letra(palavra_secreta, letra_digitada, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        letras_iguais = letra_digitada == letra
        if letras_iguais:
            letras_acertadas[index] = letra_digitada
        index += 1


def atualiza_interface(letras_acertadas,erros):
    if erros == 0:
        print("|=====|\n|     |\n|\n|\n|\n|")  # nada
    elif erros == 1:
        print("|=====|\n|     |\n|     0\n|\n|\n|")  # cabeça
    elif erros == 2:
        print("|=====|\n|     |\n|     0\n|     |\n|\n|")  # dorso
    elif erros == 3:
        print("|=====|\n|     |\n|     0\n|    /|\n|\n|")  # braço esquerdo
    elif erros == 4:
        print("|=====|\n|     |\n|     0\n|    /|\\\n|\n|")  # braço direito
    elif erros == 5:
        print("|=====|\n|     |\n|     0\n|    /|\\\n|    /\n|")  # perna esquerda
    elif erros == 6:
        print("|=====|\n|     |\n|     0\n|    /|\\\n|    / \\\n|")  # perna direita
    print("Palavra: ", end=' ')
    for letra in letras_acertadas:
        print(letra, end=' ')
    print()
    print()


def errou_uma_letra(erros):
    erros += 1

    return erros


def verifica_letra_digitada(letras_chutadas):
    letra_digitada = input("Digite uma letra: ").upper().strip()
    letra_repetida = letra_digitada in letras_chutadas
    while letra_repetida:
        print("Você já digitou a letra {}.".format(letra_digitada))
        letra_digitada = input("Digite outra letra: ").upper().strip()
        letra_repetida = letra_digitada in letras_chutadas
    letras_chutadas.append(letra_digitada)
    return letra_digitada


def inicia_interface(palavra_secreta):
    print("|=====|\n|     |\n|\n|\n|\n|")  # nada

    print("Palavra:", end=' ')
    for letra in palavra_secreta:
        print("_", end=' ')

    print()
    print()


def vinheta():
    print('********************************')
    print('***Bem vindo ao jogo da forca***')
    print('********************************')
    print()
    print()


def carrega_palavra_secreta():
    lista_palavras = []
    arquivo = open("C:\\Users\\sergi\\Documents\\Estudos\\PycharmProjects\\Jogo_da_forca_e_adivinhacao\\frutas.txt", "r", encoding="utf-8")
    for linha in arquivo:
        lista_palavras.append(linha.upper().strip())
    arquivo.close()

    indice_aleatorio = random.randrange(0,len(lista_palavras))
    palavra_secreta = lista_palavras[indice_aleatorio]
    return palavra_secreta


if __name__ == '__main__':
    jogar_forca()
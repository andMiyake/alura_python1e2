import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #enquanto nao enforcou E nao
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        #para o while se errar 7 vezes
        enforcou = erros == 7

        #para o while se acertar a palavra
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do Jogo")


def imprime_mensagem_abertura():
    print("********************************")
    print("***Bem vindo ao jogo da Forca***")
    print("********************************")

#Formas de chamar a função
# carrega_palavra_secreta()
# carrega_palavra_secreta("frutas.txt")
# carrega_palavra_secreta(nome_arquivo="frutas.txt")
# carrega_palavra_secreta(5) ***ERRADO o compilador vai considerar nome_arquivo como 5***
# carrega_palavra_secreta(primeira_linha_valida=5)
# carrega_palavra_secreta(nome_arquivo="frutas.txt", primeira_linha_valida= 5)

def carrega_palavra_secreta(nome_arquivo = "palavra.txt", primeira_linha_valida = 0):
    # with open("palavra.txt", "r") as arquivo
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())

    arquivo.close()

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

# def carrega_palavra_secreta(nome_arquivo = "palavra.txt"):
#     # with open("palavra.txt", "r") as arquivo
#     arquivo = open("palavra.txt", "r")
#     palavras = []
#
#     for linha in arquivo:
#         palavras.append(linha.strip().upper())
#
#     arquivo.close()
#
#     numero = random.randrange(0, len(palavras))
#     palavra_secreta = palavras[numero]
#     return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?").strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()

#tuple's são listas imutáveis.
#tuple = (0,1,2,3)
#lista = [0,1,2,3]
#set = {0,1,2,3}    não possui índice

#List Comprehension
#inteiros = [1,2,3,4,5,6]
#pares = [num for num in inteiros if x % 2 == 0]
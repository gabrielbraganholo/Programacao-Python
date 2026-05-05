from jogador import *


def popular_lista(lista, base):

    arquivo = open(base, "r", encoding="utf8")

    for item in arquivo:
        vetor_linha = item.strip().split(";")
        obj = Jogador(vetor_linha[0], vetor_linha[1], int(vetor_linha[2]), int(vetor_linha[3]), int(vetor_linha[4]))

        if obj not in lista:
            lista.append(obj)

    arquivo.close()


def exibir_lista(lista):

    for item in lista:
        print(item.dicionario())


def calculo_kda(lista):

    lista_kda = []

    for item in lista:
        if item.deaths == 0:
            kda = item.kills
        elif item.deaths > 0:
            kda = item.kills / item.deaths

        lista_kda.append(kda)

    return lista_kda

def exibir_kda(lista, lista_kda):

    print("\n---------------KDAs---------------\n")

    for i in range(len(lista_kda)):
        print(f"{lista[i].nome} | {lista_kda[i]:.1f}")


def filtrar_classe(classe, lista):

    print(" ")

    for item in lista:
        if classe.capitalize() == item.classe:
            print(item.nome)


def destaques_partida(lista, lista_kda):
    
    print("--------Destaques da Partida--------\n")

    print("-------------Maior Dano-------------\n")
    maior_dano = 0

    for item in lista:
        if item.dano_causado > maior_dano:
            maior_dano = item.dano_causado
            
    for item in lista:
        if maior_dano == item.dano_causado:
            print(f"nome: {item.nome} dano: {item.dano_causado}")

    print("\n-----------Média de Kills-----------\n")

    total_kills = 0

    for item in lista:
        total_kills += item.kills

    media_kills = total_kills / len(lista)

    print(f"média de  kills na partida: {media_kills}")

    print("\n--------------KDA > 2.0--------------\n")

    for i in range(len(lista_kda)):
        if lista_kda[i] >= 2:
            print(f"{lista[i].nome.upper()} | {lista_kda[i]:.1f}")
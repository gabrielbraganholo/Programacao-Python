from funcoes import *


base = "base.csv"
jogadores = []

popular_lista(jogadores, base)
exibir_lista(jogadores)

lista_kda = calculo_kda(jogadores)
exibir_kda(jogadores, lista_kda)

classe = input("\nDigite a classe que você deseja procurar por jogadores: ")
filtrar_classe(classe, jogadores)

destaques_partida(jogadores, lista_kda)
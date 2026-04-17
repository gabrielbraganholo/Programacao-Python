from inflacao import *


#de 0 a 11 (um para cada mês do ano)
lista_inflacao = []

Inflacao.preencher_valores_inflacao(lista_inflacao, 4, 10)
Inflacao.exibir_lista(lista_inflacao)

valor_max, mes_max = Inflacao.calcular_max(lista_inflacao)
valor_min, mes_min = Inflacao.calcular_min(lista_inflacao)

Inflacao.exibir_dados(lista_inflacao, valor_min, mes_min, valor_max, mes_max)
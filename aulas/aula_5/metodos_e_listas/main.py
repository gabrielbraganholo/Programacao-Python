from lista import *

lista_numeros_aleatorios = []

Lista.popular_lista(lista_numeros_aleatorios, 20)
Lista.exibir_lista(lista_numeros_aleatorios)

lista_pares = []
lista_impares = []

Lista.copiar_numeros(lista_numeros_aleatorios, lista_pares, lista_impares)

Lista.exibir_lista(lista_pares)
Lista.exibir_lista(lista_impares)
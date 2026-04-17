import random

class Lista:

    def popular_lista(lista, tamanho):
        for _ in range(tamanho):
            lista.append(random.randint(100, 200))
    
    def reitrar_repetidos(lista):
        nova_lista = []

        for item in lista:
            if item not in nova_lista:
                nova_lista.append(item)

        return nova_lista
    
    def exibir_lista(lista):
        for item in lista:
            print(item)

        print(f"Quantidade de números: {len(lista)}")
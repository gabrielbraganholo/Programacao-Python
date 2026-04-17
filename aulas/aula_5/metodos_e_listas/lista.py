import random

class Lista:

    def popular_lista(lista, quantidade):
        for i in range(quantidade):
            lista.append(random.randint(1, 100))

    def exibir_lista(lista):
        for item in lista:
            print(item)

        print(f"\n Total de itens: {len(lista)} \n")

    def copiar_numeros(lista, lista_par, lista_impar):
        for item in lista:
            if item % 2 == 0:
                lista_par.append(item)
            else:
                lista_impar.append(item)
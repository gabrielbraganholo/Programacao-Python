import random 


class Inflacao:

    meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
    ]

    def preencher_valores_inflacao(lista, infla_min, infla_max):
        for _ in range(12):
            lista.append(random.randint(infla_min, infla_max))

    def exibir_lista(lista):
        for i, item in enumerate(lista):
            print(f"Mês: {Inflacao.meses[i]} | Valor: {item}")
        print("\n")

    def calcular_min(lista):
        valor_min = 10
        mes = 0

        for i, item in enumerate(lista):
            if item < valor_min:
                valor_min = item
                mes = i

        return valor_min, mes

    def calcular_max(lista):
        valor_max = 4
        mes = 0

        for i, item in enumerate(lista):
            if item > valor_max:
                valor_max = item
                mes = i

        return valor_max, mes
    
    def exibir_dados(lista, valor_min, mes_min, valor_max, mes_max):
        for i, item in enumerate(lista):
            print(f"Mês: {Inflacao.meses[i]} | Valor: {item}")
        
        print(f"Valor máximo: {valor_max} | Mês: {Inflacao.meses[mes_max]}")
        print(f"Valor mínimo: {valor_min} | Mês: {Inflacao.meses[mes_min]}")
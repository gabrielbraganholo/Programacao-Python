class Leitor:

    @staticmethod
    def carregar_palavras(banco):
        palavras = []

        arquivo = open(banco, "r", encoding="utf-8")

        for linha in arquivo:
            palavra = linha.strip().lower()
            if palavra != '':
                palavras.append(palavra)

        arquivo.close()

        return palavras
    
    @staticmethod
    def contem_palavras_prejorativas(frase, lista_prejorativa):
        frase = frase.replace(".", " ")
        frase = frase.replace(",", " ")
        frase = frase.replace("!", " ")
        frase = frase.replace("?", " ")

        palavras_frase = frase.lower().split()

        for item in palavras_frase:
            if item in lista_prejorativa:
                return True
            
        return False
    
    @staticmethod
    def ocorrencia_prejorativa(frase, lista_prejorativa, contador):
        frase = frase.replace(".", " ")
        frase = frase.replace(",", " ")
        frase = frase.replace("!", " ")
        frase = frase.replace("?", " ")

        palavras_frase = frase.lower().split()

        for item in palavras_frase:
            if item in lista_prejorativa:
                if item in contador:
                    contador[item] += 1
                else:
                    contador[item] = 1

    @staticmethod
    def exibir_listas(lista_prejorativa, lista_boa, contador):
        print("---------- Comentários Prejorativos ----------")
        for item in lista_prejorativa:
            print("-> ", item)

        print("-------------- Comentários Bons --------------")
        for item in lista_boa:
            print("-> ", item)

        print("---------- Ocorrência Prejorativas -----------")
        for item, quantidade in contador.items():
            print("-> ", item, ":", quantidade)

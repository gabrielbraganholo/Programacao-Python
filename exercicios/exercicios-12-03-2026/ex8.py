lista_dados_originais = []
valor = 1
print("Digite 0 para parar de digitar valores.")

while(valor != 0):
    valor = int(input("Valor de glicemia: "))

    if(valor<45 or valor>450):
        print("O valor deve ser maior que 45 e menor que 450.\nDigite novamente: ")
    else:
        lista_dados_originais.append(valor)

for item in lista_dados_originais:
    print(item)
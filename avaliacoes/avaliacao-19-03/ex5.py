media_temperatura = 0
quantidade_dias = int(input("Digite a quantidade de dias você deseja analisar: "))
contador = 0
total_temperatura = 0

while(contador<quantidade_dias):
    temperatura = int(input(f"Digite a temperatura do dia {contador+1}: "))
    total_temperatura += temperatura

    contador += 1

media_temperatura = int(total_temperatura/quantidade_dias)

print(f"Média aritimética das temperaturas: {media_temperatura}Cº")

if(media_temperatura>25):
    print("Acima do esperado.")
else:
    print("Dentro da normalidade")
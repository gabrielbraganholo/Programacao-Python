nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1+nota2)/2

if(media>=7):
    print("Aprovado.")
if(media<=3):
    print("Reprovadoo.")
if(media > 3 and media < 7):
    print("Em exame.")
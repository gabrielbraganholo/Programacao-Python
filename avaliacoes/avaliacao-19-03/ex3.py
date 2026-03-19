flag = 0

print("Digite um valor negativo para encerrar o programa.")
while(flag == 0):
    nivel_rio = int(input("Digite o nivel do rio em metros: "))

    if(0 <= nivel_rio < 3):
        print("Estado normal.")
    elif(3 <= nivel_rio <= 5):
        print("Estado de alerta.")
    elif(nivel_rio > 5):
        print("Evacuação imediata.")
    elif(nivel_rio<0):
        flag = 1
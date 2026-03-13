glicemia_momento = int(input("Digite a dua glicemia do momento: "))
meta_pre_refeicao = int(input("Meta pos refeição: "))
fator_sensibilidade = int(input("Fator de sensibilidade: "))

while(fator_sensibilidade > 60 or fator_sensibilidade < 20):
    if(fator_sensibilidade > 60):
        fator_sensibilidade = int(input("Valor não pode ser maior que 60.\nDigite novamente: "))
    if(fator_sensibilidade < 20):
        fator_sensibilidade = int(input("Valor não pode ser menor que 20.\nDigite novamente: "))

quantidade_insulina = (glicemia_momento - meta_pre_refeicao) / fator_sensibilidade

print(f"Você deve administrar {quantidade_insulina:.1f} de insulina")
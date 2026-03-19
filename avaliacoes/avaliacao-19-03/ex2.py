hp_personagem = 100
hp_monstro = 100
rodada = 1

while(hp_personagem>0 and hp_monstro>0):
    print(f"-----\nRodada {rodada}\n-----")
    dano_personagem = int(input("Digite o dano do personagem: "))
    hp_monstro -= dano_personagem
    if(hp_monstro<=0):
        break
    
    dano_monstro = 0
    while(dano_monstro<=0):
        dano_monstro = int(input("Digite o dano do monstro: "))

        if(dano_monstro<=0):
            print("O dano do mostro precisa ser maior que 0.")
        else:
            hp_personagem -= dano_monstro

    if(hp_personagem>0 and hp_monstro>0):
        rodada +=1

    print(f"Vida restante:\nHerói -> {hp_personagem}\nMonstro -> {hp_monstro}")

if(hp_personagem>0):
    if(hp_personagem==100):
        print(f"Vida restante:\nHerói -> {hp_personagem}\nMonstro -> {hp_monstro}")
        print("Vitória esmagadora do herói.")
    else:
        print("Vitória do herói.")
else:
    print("Vitória do mostro.")
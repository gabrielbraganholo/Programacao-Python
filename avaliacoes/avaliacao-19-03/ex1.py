meta_biomassa = int(input("Digite a meta de biomassa que você deseja atingir: "))
biomassa_total = 0
arvores = 0

while(meta_biomassa > biomassa_total):
    biomassa_arvore = int(input(f"Valor de biomassa da árvore {arvores+1}: "))
    biomassa_total  += biomassa_arvore
    arvores += 1

if(meta_biomassa<biomassa_total):
    print(f"Meta de biomassa atingida! {arvores} árvores foram necessárias.")


peso_total = 0

while(peso_total<=15):
    peso_item = int(input("Digite o peso, em kg, do item a ser colocado na mochila: "))
    peso_total += peso_item

    if(peso_total>15):
        peso_total -= peso_item
        print(f"Mochila cheia, item descartado!\nPeso final total: {peso_total}kg")
        break
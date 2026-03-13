siglas = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF",
    "ES", "GO", "MA", "MT", "MS", "MG",
    "PA", "PB", "PR", "PE", "PI", "RJ",
    "RN", "RS", "RO", "RR", "SC", "SP",
    "SE", "TO"
]

naturalidade = [
    "acreano", "alagoano", "amapaense", "amazonense", "baiano", "cearense", "brasiliense",
    "capixaba", "goiano", "maranhense", "mato grossense", "sul mato grossense", "mineiro",
    "paraense", "paraibano", "paranaense", "pernambucano", "piauiense", "fluminense",
    "potiguar", "gaúcho", "rondoniense", "roraimense", "catarinense", "paulista",
    "sergipano", "tocantinense"
]

estado = input("Digite a sigla do seu estado: ").upper()

while(estado not in siglas):
    estado = input("Deve ser uma sigla válida: ").upper()

for i in range(len(siglas)):
    if(estado == siglas[i]):
        print(f"Você é {naturalidade[i]}")


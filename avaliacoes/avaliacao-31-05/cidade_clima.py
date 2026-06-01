class CidadeClima:
    def __init__(self, nome, temperatura, umidade, condicao):
        self.nome = nome
        self.temperatura = temperatura
        self.umidade = umidade
        self.condicao = condicao

    def __str__(self):
        return(
            f"{'-' * 60}"
            f"Cidade: {self.nome} | Temperatura: {self.temperatura} | Umidade: {self.umidade} | Condição: {self.condicao}"
            f"{'-' * 60}"
        )
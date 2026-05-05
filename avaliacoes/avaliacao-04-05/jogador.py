class Jogador:

    def __init__(self, nome, classe, kills, deaths, dano_causado):
        self.nome = nome
        self.classe = classe
        self.kills = kills
        self.deaths = deaths
        self.dano_causado = dano_causado

    def dicionario(self):
        return {
            "nome": self.nome,
            "classe": self.classe,
            "kills": self.kills,
            "deaths": self.deaths,
            "dano": self.dano_causado
        }
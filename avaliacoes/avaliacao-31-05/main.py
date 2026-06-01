import requests
import os
from cidade_clima import CidadeClima
from dotenv import load_dotenv


load_dotenv()


def pegar_clima(cidade, api_key):
    """
    Busca os dados climáticos de uma cidade na API OpenWeatherMap.

    Args:
        cidade (str): Nome da cidade a ser consultada.
        api_key (str): Chave de acesso da API.

    Returns:
        CidadeClima || None: Objeto CidadeClima em caso de sucesso ou None em caso de erro.
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    
    # Tenta realizar a consulta na API e processar os dados retornados
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            temperatura = dados["main"]["temp"]
            umidade = dados["main"]["humidity"]
            condicao = dados["weather"][0]["description"]
            
            return CidadeClima(cidade, temperatura, umidade, condicao)
        
        # Caso o status code retornar algo diferente de 200 ele chega no print e descreve o erro
        print(f"Erro ao obter dados da cidade: {cidade}")
        
    # Captura possíveis erros durante a requisição ou processamento de dados
    except Exception as erro:
        print(f"Erro ao consultar a API: {erro}")
        
    return None


def gerar_relatorio(cidades, api_key):
    """
    Gera uma lista contendo objetos CidadeClima.

    Args:
        cidades (list): Lista de cidades a serem consultadas.
        api_key (str): Chave de acesso da API.

    Returns:
        list: Lista de objetos CidadeClima.
    """
    
    relatorio_clima = []
    
    for cidade in cidades:
        cidade_clima = pegar_clima(cidade, api_key)

        if cidade_clima is not None:
            relatorio_clima.append(cidade_clima)

    return relatorio_clima


def exibir_relatorio(relatorio_clima):
    """
    Exibe os dados climáticos armazenados na lista.

    Args:
        relatorio_clima (list): Lista de objetos CidadeClima.

    Returns:
        None: Esta função apenas exibe informações na tela.
    """
    
    print("\nRELATÓRIO CLIMÁTICO")
    print("=" * 60)
    
    for cidade in relatorio_clima:
        print(cidade)


if __name__ == "__main__":
    
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        print("API_KEY não encontrada no arquivo .env")
        exit()

    cidades_padrao = [
    "Amsterdam",
    "Dubai",
    "Berlin",
    "Mexico City",
    "Toronto"
    ]
    
    print(f"{'-' * 10} Menu {'-' * 10}\n")
    print("1 - Consultar cidades padrão\n")
    print("2 - Digitar uma cidade\n")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":

        cidades = cidades_padrao

    elif opcao == "2":

        cidade = input("Digite o nome da cidade: ")
        cidades = [cidade]

    else:
        print("Opção inválida.")
        exit()

    relatorio_clima = gerar_relatorio(cidades, api_key)

    exibir_relatorio(relatorio_clima)
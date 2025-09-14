import requests
def converter(
    valor: float,
    de: str,
    para: str) -> float:

    url = f"https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/{de}"

    resposta = requests.get(url)

    dados = resposta.json()

    taxa = dados['conversion_rates'][para]
    return valor * taxa




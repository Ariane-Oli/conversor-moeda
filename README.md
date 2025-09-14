# 📖 Coin Converter 
1. Visão Geral

O Coin Converter é uma ferramenta simples em Python que converte valores entre diferentes moedas usando a API gratuita ExchangeRate-API.
Ela recebe um valor, a moeda de origem e a moeda de destino, e retorna o valor convertido.

2. Tecnologias

Python 3.12

Biblioteca requests

API: [ExchangeRate-API](https://www.exchangerate-api.com/)


3. Estrutura do Projeto
```bash 
coin-converter/
│
├─ converter.py       # Função principal de conversão
├─ README.md          # Documentação do projeto
└─ requirements.txt   # Dependências do projeto
```

1.Clone o repositório:
```bash
git clone https://github.com/seu-usuario/coin-converter.git
cd coin-converter
```
2. Instale as dependências:
``` bash
pip install -r requirements.txt
```
3. Certifique-se de ter o requests instalado:
``` bash
pip install requests
```
4. Exemplo de Uso
``` python
from converter import converter

valor_convertido = converter(100, "USD", "BRL")
print(f"100 USD em BRL: {valor_convertido:.2f}")
```
Saída esperada:
``` css
100 USD em BRL: 539.14
```

5. Testando a API no Insomnia

1. Crie uma requisição GET no Insomnia.

2. Use a URL:
``` bash
https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD
```
3. Clique em Send.

4. Você verá o JSON com as taxas de câmbio em "conversion_rates".

5. Para converter outro valor ou moeda, basta alterar o parâmetro base na URL (USD) e pegar a taxa correspondente.

8. Observações
- Substitua YOUR-API-KEY pela sua chave gratuita obtida no site da [ExchangeRate-API](https://www.exchangerate-api.com/)

- Certifique-se de que a moeda de destino existe no JSON retornado.

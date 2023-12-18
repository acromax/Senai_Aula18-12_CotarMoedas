# COtação de moedas

import requests


def getCotacao(codMoeda):
    try:
        requisicao.get(f'https://economia.awesomeapi.com.br/json/last{codMoeda}-BRL')

    cotacao = requisicao_dic[f'{codMoeda}BRL'['bid']]
    return cotacao

    except:
    print('Código de moeda inválido!')
    return None

# Dicionário
requisicao_dic = requisicao.json()


# Cotação
print(f'\nUSD 1.00 = R$ {getCotacao("USD")}')
print(f'\nEUR 1.00 = R$ {getCotacao("EUR")}')
print(f'\nBTC 1.00 = R$ {getCotacao("BTC")}')
yaq
'''
Crie um programa que receba uma URL e
execute um método GET exibindo como
saída:
– Status code;
– Cabeçalhos (response headers);
– Tamanho da resposta (content length);
– O corpo da resposta.
'''

import requests


def main():
    url = 'http://www.ifpi.edu.br/'
    response = requests.get(url)
    mostraInformacoes(response)


def mostraInformacoes(response):
    print(response.status_code)
    print(response.headers['content-type'])
    print(response.text)
    print(len(response.text), 'bytes')


if __name__ == '__main__':
    main()

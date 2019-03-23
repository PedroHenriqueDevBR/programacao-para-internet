'''
Crie um programa em que permita baixar, via
HTTP e usando o método GET, um arquivo de
imagem (escolha um tipo apenas - jpg ou gif...):
• Passe como parâmetro o "endereço WEB" completo até o arquivo;
• Salve o corpo da resposta como um arquivo atentando para o tipo.
'''

import requests as req
import urllib.request


def main():
    url = 'https://python.rs/pylogo.png'
    name = url.split('/')[-1]
    urllib.request.urlretrieve(url, name)


if __name__ == '__main__':
    main()

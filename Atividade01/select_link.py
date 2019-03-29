'''
Receba uma URL de uma página WEB como
entrada;
• Execute uma chamada usando o método GET para a URL;
• Efetue um "parse" na página obtida e gere um arquivo texto com todos os links presentes na
    página: atributos href contidos dentro de tags <a></a>
    Ex de link: <a href="http://www.google.com">Página do Google</a>
'''


import requests as req
import re


def main():
    url = input('Digite a url para obter os links: ')
    response = req.get(url)
    links = select_all_tag_a(response.text)
    show_all(links)
    gerar_arquivo(links)


def select_all_tag_a(content):
    links = []
    result = re.findall('href="(.*)"\s', content)
    
    for elem in result:
        links.append(elem)
    
    return links


def show_all(links):
    for link in links:
        print(link)


def gerar_arquivo(lista):
    nome = input('Digite o nome do arquivo: ')
    arquivo = open('{}.txt'.format(nome), 'w')
    lista_para_salvar = []

    for linha in lista:
        lista_para_salvar.append(linha + '\n')
    
    arquivo.writelines(lista_para_salvar)
    arquivo.close()


if __name__ == '__main__':
    main()

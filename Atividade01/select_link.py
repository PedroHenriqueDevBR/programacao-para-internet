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
    url = 'http://www.ifpi.edu.br/'
    response = req.get(url)
    links = select_all_tag_a(response.text)
    show_all(links)


def select_all_tag_a(content):
    links = []

    while True:
        try:
            result = re.search('<\s*a[^>]*>(.*?)<\s*/\s*a>', content)
            found = result.group(0)
            links.append(found)
            content = content.replace(found, ' ')
        except:
            break

    return links

def show_all(links):
    for link in links:
        print(link)


if __name__ == '__main__':
    main()

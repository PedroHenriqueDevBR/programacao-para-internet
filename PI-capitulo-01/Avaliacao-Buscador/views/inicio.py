from controllers.prototipo import Indexador

# Instanciação
motor = Indexador()


def main():
    busca = input('Digite a sua busca: ')
    inicio = input('Digite a url inicial: ')
    camadas = int(input('Quantas camadas seguir: '))

    motor.seach(busca, inicio, camadas)
    sites_encontrados = motor.matchs
    mostrar_sites(sites_encontrados)


def mostrar_sites(sites):
    print('\n\n\n')
    print('Resultado da busca')
    for site in sites:
        print('---------------------------------------------')
        print(site['titulo'])
        print(site['link'])
        print(site['descricao'])
        print('---------------------------------------------')


if __name__ == '__main__':
    main()

import requests

titulo = 'naruto'
limite = '1'
url = "https://api.jikan.moe/v3/search/anime?q={titulo}&limit={limite}"
url = url.format(titulo=titulo, limite=limite)
response = requests.get(url).json()

results = response['results']

for result in range(len(results)):
    print('título: {}\n'
          'sinopse: {}\n'
          'tipo: {}\n'
          'episódios: {}\n'
          'nota: {}\n'.format(results[result]['title'],
                              results[result]['synopsis'],
                              results[result]['type'],
                              results[result]['episodes'],
                              results[result]['score'],))

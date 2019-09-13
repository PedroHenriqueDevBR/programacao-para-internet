import requests
token = '985189186:AAFHShdWIIYXi5XiaD7EHFkr19S3YD3WV8U'


def post_msg(msg):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(token)
    dados = {'chat_id': 891308791, 'text': msg}
    response = requests.post(url, data=dados)
    print(response.content)


post_msg('salve salve')

import json


def main():
    import_data()


def import_data():
    file = open('db.json')
    object = ''

    for line in file:
        object += line.strip()

    retornar = json.loads(object)

    print('Debug')
    return retornar

if __name__ == '__main__':
    main()

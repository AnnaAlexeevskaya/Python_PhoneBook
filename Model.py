phone_book = {}
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        print(data)

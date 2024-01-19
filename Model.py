phone_book = {}
path = 'phones.txt'
SEPARATOR = ';'


def open_file():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = {i: item for i, item in enumerate(list(map(lambda x: x.strip().split(SEPARATOR), file.readlines())), 1)}
    print(phone_book)   
    return phone_book


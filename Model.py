phone_book = {}
path = 'phones.txt'
SEPARATOR = ';'


def open_file():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = {i: item for i, item in enumerate(list(map(lambda x: x.strip().split(SEPARATOR), file.readlines())), 1)}
      



def save_file():
    pass

def next_id():
    global phone_book
    return (max(phone_book) + 1) if phone_book else 1


def new_contact(contact: list[str]):
    global phone_book
    phone_book[next_id()] = contact





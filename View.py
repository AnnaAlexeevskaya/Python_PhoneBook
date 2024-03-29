import text
from Model import PhoneBook, Contact



def main_menu() -> int:
    for n, item in enumerate(text.main_menu):
        if n ==0:
            print(item)
        else:
            print(f'\t{n}. {item}')
    while True:
        choice = input(text.main_menu_choice)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(f'Введите пункт меню от 1 до {len(text.main_menu)-1} ')


def show_contacts(p_book: PhoneBook, error_messsage: str):
        max_size = p_book.max_len()

        if p_book:
            print('\n' + '=' * (sum(max_size) + 9))
            for n, contact in p_book.phonebook.items():
                print(f'{n:>3}. {contact.name:<{max_size[0]}} {contact.phone:<{max_size[1]}} {contact.comment:<{max_size[2]}} ')
            print('='*(sum(max_size) + 9) + '\n')
        else:
            print_message(error_messsage)

def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message) + '\n')


def add_contact(message: list[str], contact: Contact = None) -> Contact:
    contact = contact if contact else Contact('', '', '')

    for n, mes in enumerate(message):
        field = input(mes)
        setattr(contact, ['name', 'phone', 'comment'][n], field)

    return contact


def input_data(message: str) -> str:
    return input(message)

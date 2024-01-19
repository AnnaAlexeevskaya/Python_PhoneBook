import text


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


def show_contacts(p_book: dict[int, list[str]]):
        max_size = list(map(lambda x: len(max(x, key = len)), list(zip(*p_book.values()))))
        print(max_size)
        if p_book:
            print('\n' + '=' * (sum(max_size) + 9))
            for n, contact in p_book.items():
                print(f'{n:>3}. {contact[0]:<{max_size[0]}} {contact[1]:<{max_size[1]}} {contact[2]:<{max_size[2]}} ')
            print('='*(sum(max_size) + 9) + '\n')
        else:
            print_message(text.empty_phone_book)

def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message) + '\n')



    
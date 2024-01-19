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
        for n, contact in p_book.items():
             print(f'{n}. {contact[0]} ')

    
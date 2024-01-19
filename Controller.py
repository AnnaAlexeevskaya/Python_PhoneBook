import text
import View
import Model


def start_app():
    pb = Model.phone_book
    while True:
        choice = View.main_menu()
        match choice:
            case 1:
                pb = Model.open_file()
                View.print_message(text.load_successful)
            case 2:
                pass            
            case 3:
                pb = Model.phone_book
                View.show_contacts(pb)            
            case 4:
                contact = View.add_contact(text.ew_contact)
                Model.new_contact(contact)
                View.print_message(text.new_contact_added_successful(contact[0]))            
            case 5:
                pass            
            case 6:
                pass            
            case 7:
                pass
            case 8:
                break
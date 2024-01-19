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
            case 2:
                pass            
            case 3:
                View.show_contacts(pb)            
            case 4:
                pass            
            case 5:
                pass            
            case 6:
                pass            
            case 7:
                pass
            case 8:
                break
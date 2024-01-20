import text
import View
import Model

def find_contact():



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
                View.show_contacts(pb, text.empty_phone_book)            
            case 4:
                contact = View.add_contact(text.new_contact)
                Model.new_contact(contact)
                View.print_message(text.new_contact_added_successful(contact[0]))            
            case 5:
                # word = View.input_data(text.input_search_word)
                # result = Model.find_contact(word)
                # View.show_contacts(result, text.contacts_not_found(word))        
                find_contact()
            case 6:
                find_contact()
                pb = Model.phone_book
                c_id = int(View.input_data(text.input_id_change_contact))
                c_contact = View.add_contact(text.change_contact, pb[c_id])
                Model.change_contact(c_id, c_contact)  
                View.print_message(text.contact_changed_successful(c_contact[0]))       
            case 7:
                pass
            case 8:
                break
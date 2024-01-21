import text
import View
import Model
from Model import Contact, PhoneBook

def find_contact(phones: Model.PhoneBook):
    word = View.input_data(text.input_search_word)
    result = phones.find_contact(word)
    View.show_contacts(result, text.contacts_not_found(word))


def start_app():
    pb = Model.PhoneBook()
    while True:
        choice = View.main_menu()
        match choice:
            case 1:
                pb.open_file()
                View.print_message(text.load_successful)
            case 2:
                pb.save_file()
                View.print_message(text.save_successful)
            case 3:
                View.show_contacts(pb, text.empty_phone_book)
            case 4:
                contact = View.add_contact(text.new_contact)
                pb.new_contact(contact)
                View.print_message(text.new_contact_added_successful(contact[0]))
            case 5:
                find_contact(pb)
            case 6:
                find_contact(pb)
                c_id = int(View.input_data(text.input_id_change_contact))
                c_contact = View.add_contact(text.change_contact, pb.phonebook[c_id])
                pb.change_contact(c_id, c_contact)
                View.print_message(text.contact_changed_successful(c_contact[0]))
            case 7:
                find_contact(pb)
                c_id = int(View.input_data(text.input_id_delete_contact))
                name = pb.delete_contact(c_id).name
                View.print_message(text.contact_deleted_successful(name))
            case 8:
                View.print_message(text.good_bye)
                break

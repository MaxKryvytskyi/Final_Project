
from address_book1 import PersonName, PersonPhoneNumbers, PersonAddress, PersonEmailAddress, PersonBirthday, PersonNote, PersonStatus, Person, AddressBook
from my_exception import ExceptionIncorrectFormat
from log import log

# Відповідає за те загрузити стару книгу чи створити нову
def start_work_bot(adress_book: AddressBook):
    while True:
        try:
            user_input = input(log("Download contact book? Y/N ---> ", "[Bot's answer] ")).lower()
            log(user_input, "[User input] ")
            if user_input in "y n":
                if user_input == "y":
                    print(log("Downloading the contact book...", "[Bot's answer] "))
                    return adress_book.load_address_book()
                elif user_input == "n":
                    print(log("Creates new contact book...", "[Bot's answer] "))
                    return adress_book
            else:
                print(log("The command is not recognized", "[Bot's answer] "))
                continue
        except UnicodeEncodeError:
            continue

# Обробка помилок.
def input_error(func):
    def inner(*argsi,**kwargs): 
        try:
            return func(*argsi,**kwargs)
        except TypeError: return f"Wrong command"
        except IndexError: return f"Enter name and phone separated by a space!"
        except ValueError: return f"Incorrect data"
        except KeyError: return f"Enter another name."
        except AttributeError: return f"Enter command."
        except ExceptionIncorrectFormat as error: return error
        except KeyboardInterrupt: return exit()
    return inner

# ======================================================================================================
# =========================================[ add ]======================================================
# ======================================================================================================

@input_error
def add(*_: str) -> str:
    while True:  
        name = input("Введіть ім'я контакту \n---> ").capitalize()
        if name in adress_book.keys(): print("Name Error. Контакт с таким ім'ям вже створено")
        else: break
    phone = input("Введіть телефон контакту \n---> ") 
    email = input("Введіть електронну почту контакту \n---> ")
    birthday = input("Введіть день народження контакту \n---> ")
    status = input("Введіть статус контакту \n---> ")
    city = input("Введіть місто де проживає контакт \n---> ")
    street = input("Введіть вулицю де проживає контакт \n---> ")
    house = input("Введіть номер будинку де проживає контакт \n---> ")
    note = input("Введіть нотатку про контакт \n---> ")
    person = Person(PersonName(name), PersonPhoneNumbers(phone), PersonEmailAddress(email), PersonBirthday(birthday), PersonStatus(status), PersonAddress(city, street, house), PersonNote(note))
    return adress_book.add_person(person)

@input_error
def add_phone(*args):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючі телефони {args[0].capitalize()}")
        print([phone.value_of() for phone in person.phones])
        new_phone = input("Введіть новий телефон який ви хочете додати до контакту або введіть \"exit\" Для виходу\n---> ")
        if new_phone == "exit": return "Операція прервана"
        elif new_phone in [phone.value for phone in person.phones]: print("Error Цей телефон вже існує у цього контакту")
        else: break
    person.add_phone(PersonPhoneNumbers(new_phone))

@input_error
def add_email(*args):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючі email {args[0].capitalize()}")
        print([email.value_of() for email in person.emails])
        new_email = input("Введіть новий email який ви хочете додати до контакту або введіть \"exit\" Для виходу\n---> ")
        if new_email == "exit": return "Операція прервана"
        elif new_email in [email.value for email in person.emails]: print("Error Цей email вже існує у цього контакту")
        else: break
    person.add_email(PersonEmailAddress(new_email))


# Список команд.
COMMANDS = {
    # add_status : ("add status", ), # +
    # add_note : ("add note", ), # +
    # add_birthday : ("add birthday", ), # +
    # add_address : ("add address", ), # +
    add_email : ("add email", ), 
    add_phone : ("add phone", ), 
    add : ("add", ), 
    
    # remove : ("remove", ), # +
    # change : ("change", ), # +

    # all_birthday : ("all birthday", ), # +
    # birthday : ("birthday", ), # +
    # exit_uzer : ("close", "exit", "good bye"), # +
    # show_page : ("show page", ), # +
    # search : ("search", ), # +
    # helper : ("help", ), # +-
    # phone : ("phone", ), # +
    # hello : ("hello", ) # +
}


# Знаходить команду.
@input_error    
def handler(uzer_input: str):
    for command, args_com in COMMANDS.items():
        for a_com in args_com:
            if uzer_input.lower().startswith(a_com):
                if uzer_input[:len(a_com)].lower() == a_com:
                    log(f"Found command to [{a_com}], parameters to {uzer_input[len(a_com):].strip().split()}", "[Data processing] ")
                    return command, uzer_input[len(a_com):].strip().split()
    return "There is no such command", None

@input_error
def main():
    while True:
        adress_book.save_address_book(adress_book)
        uzer_input = log(input("-->"), "[User input] ")
        
        if not uzer_input:
            print(log("You have not entered anything", "[Error] "))
            continue
        com, data = handler(uzer_input)
    
        if com == "There is no such command":
            print(log(com, "[Error] "))
            continue
        print(com(*data))

if __name__ == "__main__":
    adress_book = AddressBook()
    load_book = start_work_bot(adress_book)
    if load_book: adress_book = load_book
    main()
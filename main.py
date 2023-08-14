from datetime import datetime


from fields import PersonName, PersonPhoneNumbers, PersonAddress, PersonEmailAddress, PersonBirthday, PersonNote, PersonStatus
from address_book import AddressBook
from person import Person
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
def add(*args: str):
    while True:  
        if len(args) > 0:
            name = args[0]
            if name in adress_book.keys(): 
                print(f"Name Error. Контакт с таким {name} вже створено")
                name = input("Введіть ім'я контакту \n---> ").capitalize()
        else : 
            name = input("Введіть ім'я контакту \n---> ").capitalize()
        if name in adress_book.keys(): 
            print(f"Name Error. Контакт с таким {name} вже створено")
        else: break
        
    phone = input("Введіть телефон \n---> ") 
    email = input("Введіть електронну почту \n---> ")
    birthday = input("Введіть день народження \n---> ")
    status = input("Введіть статус [work, family, friend]\n---> ")
    city = input("Введіть місто \n---> ")
    street = input("Введіть вулицю \n---> ")
    house = input("Введіть номер будинку \n---> ")
    note = input("Введіть нотатку про контакт \n---> ")
    person = Person(PersonName(name), PersonPhoneNumbers(phone), PersonEmailAddress(email), PersonBirthday(birthday), PersonStatus(status), PersonAddress(city, street, house), PersonNote(note))
    return adress_book.add_person(person)

@input_error
def add_phone(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючі Phones {args[0].capitalize()}\n{[phone.value_of() for phone in person.phones]}")
        new_phone = input("Введіть Phone або введіть \"exit\" Для виходу\n---> ")
        if new_phone == "exit": return "Операція прервана"
        elif new_phone in [phone.value for phone in person.phones]: print("Error Цей телефон вже існує у цього контакту")
        else: break
    return person.editing_phone(PersonPhoneNumbers(new_phone))

@input_error
def add_email(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючі Email {args[0].capitalize()}\n{[email.value_of() for email in person.emails]}")
        new_email = input("Введіть Email або введіть \"exit\" Для виходу\n---> ")
        if new_email == "exit": return "Операція прервана"
        elif new_email in [email.value for email in person.emails]: print("Error Цей email вже існує у цього контакту")
        else: break
    return person.editing_email(PersonEmailAddress(new_email))

@input_error
def add_birthday(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючий Birthday {args[0].capitalize()}\n{person.birthday.value_of()}")
        new_birthday = input("Введіть Birthday або введіть \"exit\" Для виходу\n---> ")
        try:
            _ = datetime.strptime(new_birthday, r'%d.%m.%Y')
        except ValueError: 
            print(f"Не правильний формат \"{new_birthday}\" очікуєтся день.місяць.рік")
            continue
        if new_birthday == "exit": return "Операція прервана"
        else: break
    return person.editing_birthday(PersonBirthday(new_birthday))


@input_error
def add_status(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючий Status {args[0].capitalize()}\n{person.status.value_of()}")
        new_status = input("Введіть Status або введіть \"exit\" Для виходу\n---> ")
        if new_status == "exit": return "Операція прервана"
        elif new_status.lower() in ["work", "family", "friend"]: break
        else: print("Не вірний тип статусу очікуєтся Work, Family або Friend")
    return person.editing_status(PersonStatus(new_status))


@input_error
def add_address(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючий Address {args[0].capitalize()}\n{person.address.value_of()}")
        city = input("Введіть місто або введіть \"exit\" Для виходу\n---> ")
        if city == "exit": return "Операція прервана"
        street = input("Введіть вулицю або введіть \"exit\" Для виходу\n---> ")
        if street == "exit": return "Операція прервана"
        house = input("Введіть номер будинку або введіть \"exit\" Для виходу\n---> ")
        if house == "exit": return "Операція прервана"
        else: break
    return person.editing_address(PersonAddress(city, street, house))

@input_error
def add_note(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючий Note {args[0].capitalize()}\n{person.note.value_of()}")
        new_note = input("Введіть Note або введіть \"exit\" Для виходу\n---> ")
        if new_note == "exit": return "Операція прервана"
        elif new_note != "   ": 
            print("В Note не може бути просто пробіл")
            continue
        else: break
    return person.editing_note(PersonNote(new_note))

# ======================================================================================================
# =========================================[ del ]======================================================
# =====================================================================================================

@input_error
def del_birthday(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print(f"Вже існуючий Birthday {args[0].capitalize()}\n{person.birthday.value_of()}")
        cmd = input("Введіть \"Yes\" для видалення або \"exit\" Для виходу\n---> ")
        if cmd == "exit": return "Операція прервана"
        elif cmd.lower() == "yes": break
        else: print("Спробуйтте ще раз")
    return person.editing_birthday(PersonNote("none"))


# Список команд.
COMMANDS = {
    add_birthday : ("add birthday", ), 
    add_address : ("add address", ),
    add_status : ("add status", ),
    add_email : ("add email", ), 
    add_phone : ("add phone", ),
    add_note : ("add note", ),  
    add : ("add", ), 
    
    del_birthday : ("del birthday", ), 
    # del_address : ("del address", ),
    # del_status : ("del status", ),
    # del_email : ("del email", ), 
    # del_phone : ("del phone", ),
    # del_note : ("del note", ),  
    # del_name : ("del name", ),



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
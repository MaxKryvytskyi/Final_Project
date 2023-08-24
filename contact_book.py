from datetime import datetime
from rich.console import Console
import re

from my_exception import ExceptionIncorrectFormat
import birthday_n_days as bd
from fields import PersonName, PersonPhoneNumbers, PersonAddress, PersonEmailAddress, PersonBirthday, PersonNote, PersonStatus
from address_book import AddressBook
from person import Person
from bot_work import input_error, print_phones, print_emails, print_address, print_birthday, print_note, print_status, print_name, works_bot, start_work_bot


adress_book = AddressBook()
# ======================================================================================================
# =========================================[ add ]======================================================
# ======================================================================================================

@input_error
def add(*args: str):
    while True:  
        if len(args) > 0:
            name = args[0].capitalize()
            if name in adress_book.keys(): 
                print(f"Name Error. Контакт {name} вже створено")
                name = input("Введіть ім'я контакту \n---> ").capitalize()
        else : 
            name = input("Введіть ім'я контакту \n---> ").capitalize()
        if name in adress_book.keys(): 
            print(f"Name Error. Контакт {name} вже створено")
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
        print_phones(person)
        new_phone = input("Введіть Phone або введіть \"exit\" Для виходу\n---> ")
        if new_phone == "exit": return "Операція прервана"
        elif new_phone in [phone.value for phone in person.phones]: print("Error Цей телефон вже існує у цього контакту")
        else: break
    return person.phone_add(PersonPhoneNumbers(new_phone))

@input_error
def add_email(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_emails(person)
        new_email = input("Введіть Email або введіть \"exit\" Для виходу\n---> ")
        if new_email == "exit": return "Операція прервана"
        elif len(new_email) < 5 and new_email != " ": raise ExceptionIncorrectFormat(f"Не правильний формат email \"{new_email}\" очікувалося m.k@gmail.com")
        elif new_email in [email.value for email in person.emails]: print("Error Цей email вже існує у цього контакту")
        else: break
    return person.email_add(PersonEmailAddress(new_email))

@input_error
def add_birthday(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_birthday(person)
        new_birthday = input("Введіть Birthday або введіть \"exit\" Для виходу\n---> ")
        if new_birthday == "exit": 
            return "Операція прервана"
        else:
            try:
                birthday = datetime.strptime(new_birthday, r'%d.%m.%Y')
            except ValueError: 
                print(f"Не правильний формат \"{new_birthday}\" очікуєтся день.місяць.рік")
                continue
        if birthday: break
    return person.birthday_add(PersonBirthday(new_birthday))

@input_error
def add_status(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_status(person)
        new_status = input("Введіть Status або введіть \"exit\" Для виходу\n---> ")
        if new_status == "exit": return "Операція прервана"
        elif new_status.lower() in ["work", "family", "friend"]: break
        else: print("Не вірний тип статусу очікуєтся Work, Family або Friend")
    return person.status_add(PersonStatus(new_status))

@input_error
def add_address(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_address(person)
        city = input("Введіть місто або введіть \"exit\" Для виходу\n---> ")
        if city == "exit": return "Операція прервана"
        street = input("Введіть вулицю або введіть \"exit\" Для виходу\n---> ")
        if street == "exit": return "Операція прервана"
        house = input("Введіть номер будинку або введіть \"exit\" Для виходу\n---> ")
        if house == "exit": return "Операція прервана"
        else: break
    return person.address_add(PersonAddress(city, street, house))

@input_error
def add_note(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_note(person)
        new_note = input("Введіть Note або введіть \"exit\" Для виходу\n---> ")
        if new_note == "exit": return "Операція прервана"
        elif len(new_note) < 3: 
            print("Note занадто короткий")
            continue
        else: break
    return person.note_add(PersonNote(new_note))

# ======================================================================================================
# =========================================[ del ]======================================================
# =====================================================================================================

@input_error
def del_birthday(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_birthday(person)
        cmd = input("Введіть \"Yes\" для видалення або \"exit\" Для виходу\n---> ")
        if cmd == "exit": return "Операція прервана"
        elif cmd.lower() == "yes": break
        else: print("Спробуйтте ще раз")
    return person.birthday_del()

@input_error
def del_address(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_address(person)
        cmd = input("Введіть \"Yes\" для видалення або \"exit\" Для виходу\n---> ")
        if cmd == "exit": return "Операція прервана"
        elif cmd.lower() == "yes": break
        else: print("Спробуйтте ще раз")
    return person.address_del()

@input_error
def del_status(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_status(person)
        cmd = input("Введіть \"Yes\" для видалення або \"exit\" Для виходу\n---> ")
        if cmd == "exit": return "Операція прервана"
        elif cmd.lower() == "yes": break
        else: print("Спробуйтте ще раз")
    return person.status_del()

@input_error
def del_email(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_emails(person)
        email = input("Введіть \"Email\" для видалення або \"exit\" Для виходу\n---> ")
        if email in [email.value for email in person.emails]:
            cmd = input("Введіть \"Yes\" для видалення або \"exit\" Для виходу\n---> ")
            if cmd == "exit": return "Операція прервана"
            elif cmd.lower() == "yes": break
            else: print("Спробуйтте ще раз")
        elif email == "exit": return "Операція прервана"
        else: print("Такого email address не існує у данного контакту")
    return person.email_del(PersonEmailAddress(email))

@input_error
def del_note(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_note(person)
        cmd = input("Введіть \"Yes\" для видалення або \"exit\" Для виходу\n---> ")
        if cmd == "exit": return "Операція прервана"
        elif cmd.lower() == "yes": break
        else: print("Спробуйтте ще раз")
    return person.note_del()

@input_error
def del_name(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_name(person)
        cmd = input("Введіть \"Yes\" для видалення або \"exit\" Для виходу\n---> ")
        if cmd == "exit": return "Операція прервана"
        elif cmd.lower() == "yes": break
        else: print("Спробуйтте ще раз")
    del adress_book[args[0].capitalize()]
    return f"{args[0].capitalize()} видалений із списку контактів"

@input_error
def del_phone(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_phones(person)
        phone = input("Введіть \"Phone\" для видалення або \"exit\" Для виходу\n---> ")
        if phone in [phone.value_of() for phone in person.phones]:
            cmd = input("Введіть \"Yes\" для видалення або \"exit\" Для виходу\n---> ")
            if cmd == "exit": return "Операція прервана"
            elif cmd.lower() == "yes": break
            else: print("Спробуйтте ще раз")
        else: print("Такого телефону не існує у данного контакту")
    return person.phone_del(PersonPhoneNumbers(phone))

# ======================================================================================================
# =========================================[ change ]===================================================
# ======================================================================================================

@input_error
def change_address(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_address(person)
        city = input("Введіть місто або \"exit\" Для виходу\n---> ")
        if city == "exit": return "Операція прервана"
        street = input("Введіть вулицю або \"exit\" Для виходу\n---> ")
        if street == "exit": return "Операція прервана"
        house = input("Введіть номер будинку або \"exit\" Для виходу\n---> ")
        if house == "exit": return "Операція прервана"
        else: break
    return person.address_change(PersonAddress(city, street, house))

@input_error
def change_status(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_status(person)
        new_status = input("Введіть Status або \"exit\" Для виходу\n---> ")
        if new_status == "exit": return "Операція прервана"
        elif new_status.lower() in ["work", "family", "friend"]: break
        else: print("Не вірний тип статусу очікуєтся Work, Family або Friend")
    return person.status_change(PersonStatus(new_status))

@input_error
def change_email(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_emails(person)
        email = input("Введіть Email для зміни або введіть \"exit\" Для виходу\n---> ")
        if email == "exit": return "Операція прервана"
        elif len(email) < 5 and new_email != " ": raise ExceptionIncorrectFormat(f"Не правильний формат email \"{email}\" очікувалося m.k@gmail.com")
        new_email = input("Введіть змінений Email або введіть \"exit\" Для виходу\n---> ")
        if new_email == "exit": return "Операція прервана"
        elif len(new_email) < 5 and new_email != " ": raise ExceptionIncorrectFormat(f"Не правильний формат email \"{new_email}\" очікувалося m.k@gmail.com")
        elif new_email in [email.value for email in person.emails]: print("Error Цей email вже існує у цього контакту")
        else: break
    return person.email_change(PersonEmailAddress(email), PersonEmailAddress(new_email))

@input_error
def change_phone(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_phones(person)
        phone = input("Введіть Phone для зміни або введіть \"exit\" Для виходу\n---> ")
        if phone == "exit": return "Операція прервана"
        elif phone not in [phone.value for phone in person.phones]: print("Error Цього телефону не існує у цього контакту-> ")
        new_phone = input("Введіть змінений Email або введіть \"exit\" Для виходу\n---> ")
        if new_phone == "exit": return "Операція прервана"
        elif new_phone in [phone.value for phone in person.phones]: print("Error Цей телефон вже існує у цього контакту")
        else: break
    return person.phone_change(PersonPhoneNumbers(phone), PersonPhoneNumbers(new_phone))

@input_error
def change_name(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_name(person)
        name = input("Введіть \"нове ім'я\" для заміни або \"exit\" Для виходу\n---> ").capitalize()
        cmd = input("Введіть \"Yes\" для зміни або \"exit\" Для виходу\n---> ")
        if cmd == "exit": return "Операція прервана"
        elif cmd.lower() == "yes": break
        else: print("Спробуйтте ще раз")
    person.name_change(PersonName(person.name.value), PersonName(name))
    adress_book.data.pop(args[0].capitalize())
    adress_book[name] = person
    return f"Name змінено"

@input_error
def change_note(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_note(person)
        new_note = input("Введіть Note або \"exit\" Для виходу\n---> ")
        if new_note == "exit": return "Операція прервана"
        elif len(new_note) < 3: 
            print("Note занадто короткий")
            continue
        else: break
    return person.note_change(PersonNote(new_note))

@input_error
def change_birthday(*args: str):
    person = adress_book[args[0].capitalize()]
    while True:
        print_birthday(person)
        new_birthday = input("Введіть Birthday або \"exit\" Для виходу\n---> ")
        if new_birthday == "exit": 
            return "Операція прервана"
        else:
            try:
                birthday = datetime.strptime(new_birthday, r'%d.%m.%Y')
            except ValueError: 
                print(f"Не правильний формат \"{new_birthday}\" очікуєтся день.місяць.рік")
                continue
        if birthday: break
    return person.birthday_change(PersonBirthday(new_birthday))

# ======================================================================================================
# =========================================[ others ]===================================================
# ======================================================================================================

@input_error
def search(*args: str):
    if len(args[0]) < 3:
        return f"Minimum search length is 3"
    pattern = rf"{re.escape(args[0].lower())}"
    coincidence_list = []
    for k, v in adress_book.data.items():
        if re.findall(pattern, str(v).lower()): 
            coincidence_list.append(f"{k}")
    table = adress_book.search_contacts(coincidence_list)
    console = Console()
    console.print(table)
    return ""

@input_error
def all_birthday(*args: str) -> str:
    days = 7
    if args:
        days = int(args[0])
    console = Console()
    console.print(bd.main(adress_book, days))
    return f""

@input_error
def birthday(*args: str):
    person = adress_book[args[0].capitalize()]
    time = person.birthday.days_to_birthday() 
    if not time: return f"Contact {args[0].capitalize()} has no stored date of birth"
    else: return f"To the bottom of the birth of {args[0].capitalize()} remained {time}"
    
@input_error
def show_page(*args:str) -> str:
    n = 1
    count = args[0] if len(args) >= 1 else 5
    c = adress_book.iterator(int(count))
    for _ in range(1000):
        try:
            text = next(c)
            if text == None: raise StopIteration
        except StopIteration:
            if n > 1 : return "No more pages"
            else: return f"No saved contacts"
        stop = input(f"Page : {n}")

        if stop.lower() == "stop": return ""
        console = Console()
        console.print(text)
        n += 1

@input_error
def hello(*args:str):
    return "How can I help you?"

@input_error
def exit_uzer(*args:str):
    global works_bot 
    works_bot = False
    return "Good bye!"

# Список команд.
COMMANDS = {
    add_birthday : ("add birthday", ), 
    add_address : ("add address", ),
    add_status : ("add status", ),
    add_email : ("add email", ), 
    add_phone : ("add phone", ),
    add_note : ("add note", ),  
    add : ("add", ), 
    
    change_birthday : ("change birthday", ), 
    change_address : ("change address", ),
    change_status : ("change status", ),
    change_email : ("change email", ), 
    change_phone : ("change phone", ),
    change_note : ("change note", ),  
    change_name : ("change name", ),

    del_birthday : ("del birthday", ), 
    del_address : ("del address", ),
    del_status : ("del status", ),
    del_email : ("del email", ), 
    del_phone : ("del phone", ),
    del_note : ("del note", ),  
    del_name : ("del name", ),
    
    all_birthday : ("all birthday", ), 
    birthday : ("birthday", ), 
    exit_uzer : ("close", "exit", "good bye"), 
    show_page : ("show page", ), 
    search : ("search", ), 
    # helper : ("help", ), # +-
    hello : ("hello", ),
}

# Знаходить команду.
@input_error    
def handler(uzer_input: str):
    for command, args_com in COMMANDS.items():
        for a_com in args_com:
            if uzer_input.lower().startswith(a_com):
                if uzer_input[:len(a_com)].lower() == a_com:
                    f"Found command to [{a_com}], parameters to {uzer_input[len(a_com):].strip().split()}"
                    return command, uzer_input[len(a_com):].strip().split()
    return "There is no such command", None

@input_error
def main():
    while works_bot:
        print("Щоб повернутися в головне меню введіть \"leave\"")
        adress_book.save_address_book(adress_book)
        uzer_input = input("-->")
        
        if uzer_input == "leave":
            break

        if not uzer_input:
            print("You have not entered anything")
            continue
        com, data = handler(uzer_input)
    
        if com == "There is no such command":
            print(com)
            continue
        print(com(*data))

def contact_start():
    global adress_book
    load_book = start_work_bot(adress_book)
    if load_book: adress_book = load_book
    main()
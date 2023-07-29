import re

import birthday_n_days as bd
from log import log
from fields import Name, Phone, Birthday, Email, Address, Status
from record import Record
from address_book import AddressBook
from my_exception import IncorrectDateFormat, IncorrectPhoneeFormat, IncorrectEmailFormat, IncorrectNameFormat, IncorrectStatusFormat

works_bot = True
    
# Відповідає за те як саме почати роботу
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
        # except TypeError: return log(f"Wrong command", "[Error] ")
        # except IndexError: return log(f"Enter name and phone separated by a space!", "[Error] ")
        # except ValueError: return log(f"Incorrect data", "[Error] ")
        # except KeyError: return log(f"Enter another name.", "[Error] ")
        # except AttributeError: return log(f"Enter command.", "[Error] ")
        # except IncorrectDateFormat: return log(f"Incorrect date format", "[Error] ")
        # except IncorrectPhoneeFormat: return log(f"Incorrect phone format", "[Error] ")
        # except IncorrectEmailFormat: return log(f"Incorrect email format", "[Error] ") # new
        # except IncorrectNameFormat: return log(f"Incorrect name format", "[Error] ") # new
        # except IncorrectStatusFormat: return log(f"Incorrect status format", "[Error] ") # new
        except KeyboardInterrupt: return exit_uzer() # new
    return inner

# ======================================================================================================
# =========================================[ add ]======================================================
# ======================================================================================================

@input_error
def add(*args: str) -> str:  
    name = Name(args[0].capitalize())
    phone = Phone(args[1]) if len(args) >= 2 else None
    birthday = Birthday(args[2]) if len(args) >= 3 else None
    email = Email(args[3]) if len(args) >= 4 else None
    status = Status(args[4]) if len(args) >= 6 else None
    address = Address(args[5]) if len(args) >= 5 else None
    rec = Record(name, phone, birthday, email, status, address) 
    return adress_book.add_record(rec)

@input_error
def add_phone(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    return rec.add_phone(Phone(args[1]))

@input_error
def add_birthday(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    rec.add_to_birthday(Birthday(args[1])) 
    return log(f"Date of birth {args[0].capitalize()}, recorded", "[Bot's answer] ")

@input_error 
def add_email(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    email = Email(args[1])
    rec.add_email(email)
    return log(f'The contact "{args[0].capitalize()}" was updated with new email: {rec.email}', "[Bot's answer] ")

@input_error 
def add_status(*args: str) -> str: 
    rec = adress_book[args[0].capitalize()]
    status = Status(args[1])
    rec.add_status(status)
    return log(f'The contact "{args[0].capitalize()}" was updated with new status: {rec.status}', "[Bot's answer] ")

@input_error 
def add_address(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    city = input("City ---> ") 
    street = input("Street ---> ") 
    country = input("Country ---> ")
    address = Address(city, street, country)
    rec.add_address(address)
    return log(f'The contact "{args[0].capitalize()}" was updated with new address: {rec.address}', "[Bot's answer] ")

# ======================================================================================================
# =========================================[ remove ]===================================================
# ======================================================================================================

@input_error
def remove_name(*args: str) -> str:
    del adress_book[args[0].capitalize()]
    return log(f"{args[0].capitalize()} is deleted from the contact book", "[Bot's answer] ")

@input_error
def remove_phones(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    num = rec.remove_phone(Phone(args[1]))
    if num == "This contact has no phone numbers saved": return log(num, "[Bot's answer] ")
    return log(f"Phone number {args[0].capitalize()} : {num}\nDeleted", "[Bot's answer] ")

@input_error
def remove_email(*args: str) -> str:
    adress_book[args[0].capitalize()].remove_email(Email(args[1]))
    return log(f"{args[0].capitalize()}'s email has been removed from the contact list", "[Bot's answer] ")

@input_error
def remove_birthday(*args: str) -> str:
    adress_book[args[0].capitalize()].remove_birthday(Birthday(args[1]))
    return log(f"{args[0].capitalize()}'s birthday has been removed from the contact list", "[Bot's answer] ")

@input_error
def remove_status(*args: str) -> str:
    adress_book[args[0].capitalize()].remove_status(Status(args[1].capitalize()))
    return log(f'"{args[1].capitalize()}" status removed from {args[0].capitalize()}\'s profile', "[Bot's answer] ")

@input_error
def remove_address(*args: str) -> str:
    adress_book[args[0].capitalize()].remove_address()
    return log(f'address removed from {args[0].capitalize()}\'s profile', "[Bot's answer] ")

# ======================================================================================================
# =========================================[ change ]===================================================
# ======================================================================================================

@input_error
def change_name(*args: str) -> str:
    if not args[1].capitalize() is adress_book.data.keys():
        rec = adress_book[args[0].capitalize()]
        rec.change_name(Name(args[0].capitalize()), Name(args[1].capitalize()))
        adress_book.data.pop(args[0].capitalize())
        adress_book[args[1].capitalize()] = rec
        return log(f"Contact name {args[0].capitalize()}`s changed to {args[1].capitalize()}'s", "[Bot's answer] ")
    else: return log(f"Contact with the name {args[1].capitalize()}'s already exists", "[Bot's answer] ")

@input_error
def change_phone(*args: str) -> str:
    rec = adress_book.get(args[0].capitalize())
    if rec: return log(rec.change_phone(Phone(args[1]), Phone(args[2])))
    return log(f"Contact wit name {args[0].capitalize()} doesn`t exist.", "[Bot's answer] ")

@input_error
def change_birthday(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    rec.change_birthday(Birthday(args[1]), Birthday(args[2]))
    return log(f"Birthday profile {args[0].capitalize()}'s has been changed")

@input_error
def change_email(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    rec.change_email(Email(args[1]), Email(args[2]))
    return log(f"Email is profile {args[0].capitalize()}'s has been changed")

@input_error
def change_status(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    rec.change_status(Status(args[1]), Status(args[2]))
    return log(f"Status is profile {args[0].capitalize()}'s has been changed")

@input_error
def change_address(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    city = input("New City ---> ") 
    street = input("New Street ---> ") 
    country = input("New Country ---> ")
    address = Address(city, street, country)
    rec.change_address(address)
    return log(f'The contact "{args[0].capitalize()}" was updated with new address: {rec.address}', "[Bot's answer] ")

# ======================================================================================================
# =========================================[ other ]====================================================
# ======================================================================================================

@input_error
def all_birthday(*args: str) -> str:
    days = 7
    if args:
        days = int(args[0])
    return bd.main(adress_book, days)

@input_error
def phone(*args: str) -> str:
    rec = adress_book[args[0].capitalize()]
    return rec.phone_print(args[0].capitalize(), rec.phones)

@input_error
def birthday(*args: str):
    rec = adress_book[args[0].capitalize()]
    time = rec.days_to_birthday() 
    if not time: return log(f"Contact {args[0].capitalize()} has no stored date of birth", "[Bot's answer] ")
    else: return log(f"To the bottom of the birth of {args[0].capitalize()} remained {time}", "[Bot's answer] ")
    
@input_error
def show_page(*args:str) -> None:
    
    n = 1
    count = args[0] if len(args) >= 1 else 5
    c = adress_book.iterator(count)
    for _ in range(1000):
        try:
            text = next(c)
            if text == None: raise StopIteration
        except StopIteration:
            if n > 1 : return log(f"No more pages", "[Bot's answer] ")
            else: return f"No saved contacts"
        stop = input(f"Page : {n}")

        if stop.lower() == "stop": return ""
        print(text)
        n += 1

@input_error
def search(*args:str) -> str:
    if len(args[0]) < 3:
        return log(f"Minimum search length is 3", "[Error] ")
    pattern = rf"{re.escape(args[0].lower())}"
    coincidence_list = []
    for k, v in adress_book.data.items():
        if re.findall(pattern, str(v).lower()): coincidence_list.append(f"{k}")
    return log(adress_book.search_contacts(coincidence_list))

def helper(*_):
    output = ""
    count = 0

    for k, v in COMMANDS_LIST.items():
        if count == 0: output += "{:^90}\n".format(" " + "_"*90 + " ")
        else: output += "{:^90}\n".format("|" + "_"*90 + "|")
        output += "|{:^90}|\n".format(f" COMMANDS {count+1} - {k}")
        output += "{:^90}\n".format("|" + "_"*90 + "|")
        output += "|{:^90}|\n".format(v[0])
        output += "|{:^90}|\n".format(v[1])
        output += "{:^90}\n".format("|" + "_"*90 + "|")
        count += 1
    return output

def hello(*_):
    return log("How can I help you?", "[Bot's answer] ")

def exit_uzer(*_):
    global works_bot 
    works_bot = False
    return log("Good bye!", "[Bot's answer] ")
    
# Список команд Help
COMMANDS_LIST = {
    "add" : ["Команда яка додає в книгу контактів:", "Команда(add) Ім'я(...) Телефон(...) День Народження(...)"], 
    "add phone" : ["Команда яка додає номер телефону до існуючого списку контактів:", "Команда(add phone) Ім'я(...) Телефон(...)"], 
    "add birthday" : ["Команда яка додає дату дня народження до існуючого списку контактів:", "Команда(add birthday) Ім'я(...) День Народження(...)"],
    "birthday" : ["Команда яка показує скільки залишилося до дня народження існуючого списку контактів:", "Команда(birthday) Ім'я(...)"], 
    "change phone": ["Команда яка замінює в книзі контактів неактуальний телефон:", "Команда(change phone) Ім'я(...) Неактуальний Телефон(...) Актуальний Телефон(...)"], 
    "close, exit, good bye" : ["Команди які закінчують роботу асистента", "Команда(close, exit або good bye)"],
    "hello": ["Команда привітання", "Команда(hello)"],
    "help" : ["Команда з прикладами команд", "Команда(help)"], 
    "phone" : ["Команда яка з книги контактів виводить номер телефону", "Команда(phone) Ім'я(...)"], 
    "remove phone" : ["Команда яка з книги контактів видаляє номер телефону", "Команда(remove phone) Ім'я(...) Телефон(...)"],
    "show page" : ["Команда яка виводить книгу контактів посторінково", "Команда(show page) Контактів на сторінці(...)"],
    "search" : ["Команда яка виводить результат пошуку за патерном", "Команда(search) Патерн(...)"],
}

# Список команд.
COMMANDS = {
    add_birthday : ("add birthday", ), 
    add_address : ("add address", ), 
    add_status : ("add status", ), 
    add_email : ("add email", ),
    add_phone : ("add phone", ), 
    add : ("add", ), 
    
    remove_birthday : ("remove birthday", ), 
    remove_address : ("remove address", ), 
    remove_phones : ("remove phone", ), 
    remove_status : ("remove status", ), 
    remove_email : ("remove email", ), 
    remove_name : ("remove name", ), 


    change_birthday : ("change birthday", ), 
    change_address : ("change address",),
    change_status : ("change status", ),
    change_phone : ("change phone", ), 
    change_email : ("change email", ),
    change_name : ("change name", ), 
    

    all_birthday : ("all birthday", ),
    birthday : ("birthday", ), 
    exit_uzer : ("close", "exit", "good bye"), 
    show_page : ("show page", ), 
    search : ("search", ), 
    helper : ("help", ), 
    phone : ("phone", ), 
    hello : ("hello", ) 
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
    while works_bot:
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
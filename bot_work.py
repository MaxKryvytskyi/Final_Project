from datetime import datetime as dt

from address_book import AddressBook
from my_exception import ExceptionIncorrectFormat


# Обробка помилок.
def input_error(func):
    def inner(*argsi,**kwargs): 
        try:
            return func(*argsi,**kwargs)
        # except TypeError: return f"Wrong command"
        # except IndexError: return f"Enter name and phone separated by a space!"
        # except ValueError: return f"Incorrect data"
        # except KeyError: return f"Enter another name."
        # except AttributeError: return f"Enter command."
        except ExceptionIncorrectFormat as error: return error
        except KeyboardInterrupt: return exit()
    return inner

# Логування
def log(args, message=""):
    with open("log.txt", "a") as fn:
        date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        fn.write(f"[{date}] {message}{args}\n")
        return args
    

# Відповідає за те загрузити стару книгу чи створити нову
@input_error  
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


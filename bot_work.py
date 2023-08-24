from datetime import datetime as dt
from rich.console import Console
from rich.table import Table


from address_book import AddressBook
from note_book import NoteBook
from my_exception import ExceptionIncorrectFormat

works_bot = True

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

@input_error
def log(args, message=""):
    with open("log.txt", "a") as fn:
        date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        fn.write(f"[{date}] {message}{args}\n")
        return args
    

# Відповідає за те загрузити стару книгу чи створити нову
@input_error  
def start_work_bot(book: AddressBook | NoteBook):
    while True:
        try:
            user_input = input("Download book? Y/N ---> ").lower()
            
            if user_input in "y n":
                if user_input == "y":
                    print("Downloading the book...")
                    return book.load_address_book()
                elif user_input == "n":
                    print("Creates new book...")
                    return book
            else:
                print("The command is not recognized")
                continue
        except UnicodeEncodeError:
            continue


def print_name(person):
    table = Table(title=f"{person.name.value_of()}")

    table.add_column("Name", justify="center", style="cyan", no_wrap=True)
    table.add_column("Phones", justify="center", style="magenta", no_wrap=True)
    table.add_column("Emails", justify="center", style="cyan", no_wrap=True)
    table.add_column("Birthday", justify="center", style="cyan", no_wrap=True)
    table.add_column("Status", justify="center", style="cyan", no_wrap=True)
    table.add_column("Address", justify="center", style="cyan", no_wrap=True)
    table.add_column("Note", justify="center", style="cyan", no_wrap=True)

    table.add_row(f"{person.name.value_of()}", 
                    f"{[el.value_of() for el in person.phones] if [el.value_of() for el in person.phones] != [''] else ''}", 
                    f"{[el.value_of() for el in person.emails] if [el.value_of() for el in person.emails] != [''] else ''}",
                    f"{person.birthday.value_of()}",
                    f"{person.status.value_of()}",
                    f"{person.address.value_of()}",
                    f"{person.note.value_of()}")

    console = Console()
    console.print(table)


def print_phones(person):
    table = Table(title=f"{person.name.value_of()}")
    table.add_column("Phones", justify="center", style="cyan", no_wrap=True)
    table.add_row(f"{[el.value_of() for el in person.phones] if [el.value_of() for el in person.phones] != [''] else ''}")
    console = Console()
    console.print(table)


def print_emails(person):
    table = Table(title=f"{person.name.value_of()}")
    table.add_column("Emails", justify="center", style="cyan", no_wrap=True)
    table.add_row(f"{[el.value_of() for el in person.emails] if [el.value_of() for el in person.emails] != [''] else ''}")
    console = Console()
    console.print(table)


def print_address(person):
    table = Table(title=f"{person.name.value_of()}")
    table.add_column("Address", justify="center", style="cyan", no_wrap=True)
    table.add_row(f"{person.address.value_of()}")
    console = Console()
    console.print(table)


def print_birthday(person):
    table = Table(title=f"{person.name.value_of()}")
    table.add_column("Birthday", justify="center", style="cyan", no_wrap=True)
    table.add_row(f"{person.birthday.value_of()}")
    console = Console()
    console.print(table)


def print_note(person):
    table = Table(title=f"{person.name.value_of()}")
    table.add_column("Note", justify="center", style="cyan", no_wrap=True)
    table.add_row(f"{person.note.value_of()}")
    console = Console()
    console.print(table)


def print_status(person):
    table = Table(title=f"{person.name.value_of()}")
    table.add_column("Status", justify="center", style="cyan", no_wrap=True)
    table.add_row(f"{person.status.value_of()}")
    console = Console()
    console.print(table)
from bot_work import input_error, works_bot, start_work_bot
from note_book import Note, Tag, Record, NoteBook
from rich.console import Console
import re

note_book = NoteBook()

@input_error
def add(*args: str): 
    note = input("Введіть нотатку \n---> ")
    tag = input("Введіть тег до нотатки \n---> ")
    record = Record(Note(note), Tag(tag))
    return note_book.add_note(record)

@input_error
def add_tag(*args: str):
    num = input("Введіть номер нотатки \n---> ")
    tag = input("Введіть тег який додати \n---> ")
    return note_book.add_tag(num, Tag(tag))

@input_error
def change_note(*args: str):
    num = input("Введіть номер нотатки \n---> ")
    new_note = input("Введіть нотатку \n---> ")
    note_book.change_note(num, new_note)

@input_error
def change_tag(*args: str):
    num = input("Введіть номер нотатки \n---> ")
    del_tag = input("Введіть тег який замінити \n---> ")
    new_tag = input("Введіть тег на який замінити \n---> ")
    return note_book.change_tag(num, del_tag, new_tag)

@input_error
def del_note(*args: str):
    num = input("Введіть номер нотатки для видалення \n---> ")
    return note_book.del_note(num)

@input_error
def del_tag(*args: str):
    num = input("Введіть номер нотатки \n---> ")
    tag = input("Введіть тег який додати \n---> ")
    return note_book.del_tag(num, tag)
  
@input_error
def search(*args: str):
    search = input("Minimum search length is 3 \n---> ")
    if len(search) < 3:
        return f""
    pattern = rf"{re.escape(search.lower())}"
    coincidence_list = []
    for k, v in note_book.data.items():
        if re.findall(pattern, str(v).lower()): 
            coincidence_list.append(f"{k}")
    table = note_book.search_note_book(coincidence_list)
    console = Console()
    console.print(table)
    return ""

@input_error
def show_note(*args: str):
    console = Console()
    console.print(note_book.show_all())
    return ""

COMMANDS = {
    add_tag : ("add tag", ),
    add : ("add", ),

    change_note : ("change note", ),
    change_tag : ("change tag", ),

    del_note : ("del note", ),
    del_tag : ("del tag", ),

    search : ("search", ), 
    # helper_note : ("help", ), # +-
    show_note : ("show note", ),
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
        note_book.save_address_book(note_book)
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



def note_start():
    global note_book
    load_book = start_work_bot(note_book)
    if load_book: note_book = load_book
    main()
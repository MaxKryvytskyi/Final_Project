
from rich.console import Console
from rich.table import Table

from contact_book import contact_start
from notes_book import note_start
from clean import sort_main
from bot_work import input_error

console = Console()

def info():
    table = Table(title=f"Оберіть режим роботи")
    table.add_column("Contact Book", justify="center", style="cyan", no_wrap=False)
    table.add_column("Note Book", justify="center", style="cyan", no_wrap=False)
    table.add_column("Sort Path", justify="center", style="cyan", no_wrap=False)
    table.add_row("Команда \"Contact Book\" ", "Команда \"Note Book\" ", "Команда \"Sort Path\" ")
    return table

def contact_book():
    contact_start()
    return ""

def note_book():
    note_start()
    return ""

def sort_path():
    uzer_input = input("Введіть шлях для сортування ---> ")
    if len(uzer_input) < 1:
        return f"Enter path"
    return sort_main(uzer_input)

COMMANDS = {
    contact_book : ("contact book", ), 
    note_book : ("note book", ), 
    sort_path : ("sort path", ),

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
    while True:
        console.print(info())
        uzer_input = input("---> ")
        
        if not uzer_input:
            print("You have not entered anything")
            continue
        com, data = handler(uzer_input)
    
        if com == "There is no such command":
            print(com)
            continue
        print(com(*data))
        

if __name__ == "__main__":
    main()
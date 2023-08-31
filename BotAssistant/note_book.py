from collections import UserDict
from datetime import datetime
from abc import ABC, abstractmethod
import pickle
from rich.table import Table


class AbstractView(ABC):
    
    @abstractmethod
    def value_of(self):
        pass

    @abstractmethod   
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Tag(AbstractView):
    def __init__(self, tag):
        self.tag = tag
    
    def value_of(self):
        return f"Tag : {self.tag}"
    
    def __str__(self):
        return f"{self.tag}"

    def __repr__(self):
        return f"{self.tag}"


class Note(AbstractView):
    def __init__(self, note):
        self.note = note

    def value_of(self):
        return f"Note : {self.note}"
    
    def __str__(self):
        return f"{self.note}"

    def __repr__(self):
        return f"{self.note}"
    

class Record(AbstractView):
    def __init__(self, note, tag=None) -> None:
        self.note = note
        self.tags = []
        if tag != None:
            self.tags.append(tag)
 
    def value_of(self):
        return f"Note :{self.note} Tag :{self.tags}"

    def __str__(self):
        return f"Note :{self.note} Tag :{self.tags}"

    def __repr__(self):
        return f"Note :{self.note} Tag :{self.tags}"
    

class NoteBook(UserDict):
    def __init__(self):
        super().__init__()
        self.dict_num = {}
        self.dict_keys = {}

    def add_note(self, record):
        self.data[datetime.now().timestamp()] = record
        self.normal_keys()
        return f"Нотатка додана"

    def add_tag(self, num, new_tag):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            value = self.data[float(keys)]
            value.tags.append(new_tag)
            self.normal_keys()
            return f"Тег \"{new_tag}\" додано"
        else: return f"Такої нотатки \"{num}\" не знайдено"

    def del_tag(self, num, del_tag):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            value = self.data[float(keys)]
            for n, k in enumerate(value.tags):
                if str(k) == del_tag:
                    del value.tags[n]
                    self.normal_keys()
                    return f"Тег \"{del_tag}\" видалено"
            return f"Тег \"{del_tag}\" Не знайдено"
        else: return f"Такої нотатки \"{num}\" не знайдено"

    def change_tag(self, num, del_tag, new_tag):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            value = self.data[float(keys)]
            for n, k in enumerate(value.tags):
                if str(k) == str(del_tag):
                    value.tags[n] = new_tag
                    self.normal_keys()
                    return f"Тег \"{del_tag}\" змінено на \"{new_tag}\""
            return f"Тег \"{del_tag}\" Не знайдено"
        else: return f"Такої нотатки \"{num}\" не знайдено"

    def change_note(self, num, new_note):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            del_note = self.data[float(keys)]
            self.data[float(keys)] == new_note
            self.normal_keys()
            return f"Нотатка \"{del_note}\" змінена на \"{new_note}\""
        else: return f"Такої нотатки \"{num}\" не знайдено"

    def del_note(self, num):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            del self.data[float(keys)]
            self.normal_keys()
            return f"Нотатка \"{num}\" видалена"

    def normal_keys(self):
        for num, keys in enumerate(self.data.keys()):
            self.dict_num[str(keys)] = str(num)
            self.dict_keys[str(num)] = str(keys)

    def show_all(self):
        table = Table(title=f"Note Book")
        table.add_column("Num", justify="center", style="cyan", no_wrap=False)
        table.add_column("Tag", justify="center", style="cyan", no_wrap=False)
        table.add_column("Note", justify="center", style="cyan", no_wrap=False)
  
        for num, record in self.data.items():
            table.add_row(f"{self.dict_num[str(num)]}", 
                          f"{record.tags}",
                          f"{record.note}")
        return table
    
    def search_note_book(self, name:list) -> str:
        if name:
            table = Table(title=f"Coincides {len(name)}")
            table.add_column("Num", justify="center", style="cyan", no_wrap=False)
            table.add_column("Tag", justify="center", style="cyan", no_wrap=False)
            table.add_column("Note", justify="center", style="cyan", no_wrap=False)
            for num in name:
                keys = self.dict_num.get(str(num))
                table.add_row(f"{keys}", 
                            f"{self.data[float(num)].tags}",
                            f"{self.data[float(num)].note}")
            return table
        else: return f"Нічого не знайдено"
        
    # Зберігає книгу контактів
    def save_address_book(self, note_book):
        with open("Save_note_book.bin", "wb") as file:
            pickle.dump(note_book, file)

    # Відповідає за завантаження книги контактів яку зберегли минулого разу
    def load_address_book(self): 
        with open("Save_note_book.bin", "rb") as file:
            deserialized_note_book = pickle.load(file)
            return deserialized_note_book
        

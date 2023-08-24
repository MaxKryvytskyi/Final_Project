from collections import UserDict
from datetime import datetime
from abc import ABC, abstractmethod
from time import sleep

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
        return f"Нотатка додана"

    def add_tag(self, num, new_tag):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            value = self.data[float(keys)]
            value.tags.append(Tag(new_tag))
            return f"Тег \"{new_tag}\" додано"
        else: return f"Такої нотатки \"{num}\" не знайдено"

    def del_tag(self, num, del_tag):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            value = self.data[float(keys)]
            for n, k in enumerate(value.tags):
                if str(k) == del_tag:
                    del value.tags[n]
                    return f"Тег \"{del_tag}\" видалено"
            return f"Тег \"{del_tag}\" Не знайдено"
        else: return f"Такої нотатки \"{num}\" не знайдено"

    def change_tag(self, num, del_tag, new_tag):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            value = self.data[float(keys)]
            for n, k in enumerate(value.tags):
                if str(k) == del_tag:
                    value.tags[n] = new_tag
                    return f"Тег \"{del_tag}\" змінено на \"{new_tag}\""
            return f"Тег \"{del_tag}\" Не знайдено"
        else: return f"Такої нотатки \"{num}\" не знайдено"

    def change_note(self, num, new_note):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            del_note = self.data[float(keys)]
            self.data[float(keys)] == new_note
            return f"Нотатка \"{del_note}\" змінена на \"{new_note}\""
        else: return f"Такої нотатки \"{num}\" не знайдено"

    def del_note(self, num):
        keys = self.dict_keys.get(str(num))
        if float(keys) is not None and float(keys) in self.data:
            del self.data[float(keys)]

    def normal_keys(self):
        for num, keys in enumerate(self.data.keys()):
            self.dict_num[str(keys)] = str(num)
            self.dict_keys[str(num)] = str(keys)

    def show_all(self):
        for num, note in self.data.items():
            print(self.dict_num[str(num)], note)
    
    def value_of(self):
        return str(self.data.values())
    
    def note_all(self):
        return f"{self.data.items()}"



if __name__ == "__main__":
    note_book = NoteBook()
    tag = Tag("Work 0")
    note = Note("Note 0")
    tag1 = Tag("Work 1")
    note1 = Note("Note 1")
    tag2 = Tag("Work 2")
    note2 = Note("Note 2")
    tag3 = Tag("Work 3")
    note3 = Note("Note 3")
    note_book.add_note(Record(note, tag))
    sleep(0.1)
    # print("0")
    # print(note_book.value_of())
    # print(note_book.note_all())
    note_book.add_note(Record(note1, tag1))
    sleep(0.1)
    # print("1")
    # print(note_book.value_of())
    # print(note_book.note_all())
    note_book.add_note(Record(note2, tag2))
    sleep(0.1)
    # print("2")
    # print(note_book.value_of())
    # print(note_book.note_all())
    note_book.add_note(Record(note3, tag3))
    sleep(0.1)
    # print("3")
    # print(note_book.value_of())
    # print(note_book.note_all())

    # print(note_book.dict_num)
    note_book.normal_keys()
    # print(note_book.dict_num)
    # note_book.show_all()

    note_book.add_tag("2", "sawdw 01")
    note_book.show_all()
    note_book.add_tag("3", "sawdw 03")
    note_book.show_all()
    note_book.change_tag("3", "Work 3", "new Tag")
    note_book.del_tag("2", "sawdw 01")
    note_book.del_tag("2", "Work 2")
    note_book.show_all()
    # note_book.del_tag("3", "sawdw 03")
    # note_book.del_tag("2", "sawdw 01")
    # note_book.show_all()
    # note_book.del_note('3')
    # note_book.show_all()
    # note_book.del_note('1')
    # note_book.show_all()
    # note_book.del_note('2')
    # note_book.show_all()


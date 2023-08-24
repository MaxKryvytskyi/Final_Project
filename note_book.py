from collections import UserDict
from datetime import datetime


class NoteBook(UserDict):

    def add_note(self, note, tag):
        self[datetime.now().timestamp()] = [note, tag]

    def value_of(self):
        return str([[notes.value_of(), tag.value_of()] for notes, tag in [note for note in self.values()]])
    
    def note_all(self):
        return f"{[[keys, note] for keys, note in self.items()]}"


class Tag:
    def __init__(self, tag):
        self.tag = tag
    
    def value_of(self):
        return f"Tag : {self.tag}"


class Note:
    def __init__(self, note):
        self.note = note

    def value_of(self):
        return f"Note : {self.note}"

        
if __name__ == "__main__":
    note_book = NoteBook()
    tag = Tag("Work")
    note = Note("Note Note Note Note Note Note Note Note Note")
    note_book.add_note(note, tag)
    print(note_book.value_of())
    print(note_book.note_all())



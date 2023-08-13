import file
import note
import ui


def add():
    cur_note = ui.create_note()
    array = file.read_file()
    for notes in array:
        if note.note.get_id(cur_note) == note.note.get_id(notes):
            note.note.set_id(cur_note)
    array.append(cur_note)
    file.write_file(array, 'a')
    print('Note was added.')


def show(text):
    logic = True
    array = file.read_file()
    if text == 'date':
        date = input('Enter date dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(note.note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + note.note.get_id(notes))
        if text == 'date':
            logic = False
            if date in note.note.get_date(notes):
                print(note.note.map_note(notes))
    if logic == True:
        print('There is no any note.')


def edit():
    id = input('Enter note id: ')
    array = file.read_file()
    logic = True
    for notes in array:
        if id == note.note.get_id(notes):
            logic = False
            cur_note = ui.create_note()
            note.note.set_title(notes, cur_note.get_title())
            note.note.set_body(notes, cur_note.get_body())
            note.note.set_date(notes)
            print('Note was changed.')
    if logic == True:
        print('No one note with this id')
    file.write_file(array, 'a')


def delete():
    id = input('Enter note id: ')
    array = file.read_file()
    logic = True
    for notes in array:
        if id == note.note.get_id(notes):
            logic = False
            array.remove(notes)
            print('Note was deleted.')
    if logic == True:
        print('No one note with this id')
    file.write_file(array, 'a')


def show_by_id():
    id = input('Enter note id: ')
    array = file.read_file()
    logic = True
    for notes in array:
        if id == note.note.get_id(notes):
            logic = False
            print(note.note.map_note(notes))
    if logic == True:
        print('No one note with this id')
    file.write_file(array, 'a')

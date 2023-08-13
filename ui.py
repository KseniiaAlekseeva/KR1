import note


def create_note():
    title = input('Enter the note title: ')
    body = input('Enter the note description: ')
    return note.note(title=title, body=body)


def menu():
    print("\nEnter:\n\n1 - show all notes from file, \n2 - add note, \n3 - delete note, \n4 - edit note, \n5 - filter notes by date, \n6 - show note with id, \n7 - exit.\n")


def end():
    print("End of program.")

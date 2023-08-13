import note_operation as no
import ui


def run():
    input_from_user = ''
    while input_from_user != '7':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            no.show('all')
        if input_from_user == '2':
            no.add()
        if input_from_user == '3':
            no.show('all')
            no.delete()
        if input_from_user == '4':
            no.show('all')
            no.edit()
        if input_from_user == '5':
            no.show('date')
        if input_from_user == '6':
            no.show('id')
            no.show_by_id()
        if input_from_user == '7':
            ui.end()
            break

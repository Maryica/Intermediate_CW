from datetime import datetime, timedelta
from io import StringIO
import csv

file_path = 'notes.csv'


def read_file(file_name):
    result = []
    with open(file_name, 'r', encoding='utf-8', newline='') as text_file:
        note_reader = csv.reader(text_file, delimiter=';')
        for note in note_reader:
            result.append(note)
    return result


def write_file(list_notes, file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as text_file:
        csv.writer(text_file, delimiter=';').writerows(list_notes)


def write_end_file(note, file_name):
    with open(file_name, 'a', encoding='utf-8', newline='') as text_file:
        csv.writer(text_file, delimiter=';').writerow(note)


def sort_key(lst):
    return int(lst[0])


def sort_id(list_notes):
    return sorted(list_notes, key=sort_key)


def note_string(note, style='simple'):
    if style == 'simple':
        return '\n'.join(note[1:3])
    if style == 'txt':
        result = 'id заметки = ' + note[0] + '\n'
        result += 'Заголовок заметки = ' + note[1] + '\n'
        result += 'Тело заметки = ' + note[2] + '\n'
        result += 'Дата заметки = ' + note[3]
        return result
    if style == 'csv':
        output = StringIO()
        csv.writer(output, delimiter=';', lineterminator='').writerow(note)
        return output.getvalue()
    return '\n'.join(note)


def print_note(note, style='simple'):
    print(note_string(note, style), '\n')


def print_list(list_notes, style_list='simple'):
    for note in list_notes:
        print_note(note, style=style_list)


def next_id(list_notes):
    if len(list_notes) > 0:
        return int(list_notes[-1][0]) + 1
    else:
        return 1


def date_time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def show_all(file_name, style_show='simple'):
    print_list(read_file(file_name), style_list=style_show)


def edit_note(note):
    result = list()
    result.append(note[0])
    answer = input('Изменить заголовок (y/n)?')
    if answer.lower() == 'y':
        result.append(input('Введите новый заголовок: '))
    else:
        result.append(note[1])
    result.append(input('Введите новую заметку: '))
    result.append(date_time_now())
    return result


def filter_by_date(list_notes, date_filter):
    result = []
    for note in list_notes:
        if note[-1].split()[0] == date_filter:
            result.append(note)
    return result


def show_notes_filter_date(file_name, filter_date, style_show='simple'):
    print_list(filter_by_date(read_file(file_name), filter_date), style_list=style_show)


def date_now(day=0):

    return (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d')


def index_row_id(list_notes, note_id):
    dict_id = {note[0]: i for i, note in enumerate(list_notes)}
    return dict_id.get(note_id, -1)


def show_note_id(file_name, note_id, style_show):
    list_notes = read_file(file_name)
    index_row = index_row_id(list_notes, note_id)
    if index_row == -1:
        print('отсутствует')
    else:
        print_note(list_notes[index_row], style_show)


def del_id(file_name, note_id):
    list_notes = read_file(file_name)
    index_row = index_row_id(list_notes, note_id)
    if index_row == -1:
        print('отсутствует')
    else:
        new_list_notes = list_notes[:index_row] + list_notes[index_row + 1:]
        write_file(new_list_notes, file_name)
        print('удалена')


def replace_id(file_name, note_id):
    list_notes = read_file(file_name)
    index_row = index_row_id(list_notes, note_id)
    if index_row == -1:
        print(f'Заметка c id={note_id} отсутствует')
    else:
        list_notes[index_row] = edit_note(list_notes[index_row])
        write_file(list_notes, file_name)
        print(f'Заметка c id={note_id} отредактирована')


def input_number(msg):
    num = input(msg)
    try:
        n = int(num)
        return n if n > 0 else 10
    except ValueError:
        return 10


def main():
    choice = ''
    style_view = 'simple'
    while choice != '0':
        choice = input("""
        Выберите действие:
        1. Добавить заметку
        2. Показать все заметки
        3. Показать заметку по id
        4. Редактировать заметку по id
        5. Удалить заметку по id
        6. Показать заметки по дате (в формате ГГГГ-ММ-ДД)
        0. Выход
        """)
        if choice == '1':
            new_note = list()
            new_note.append(str(next_id(read_file(file_path))))
            new_note.append(input('Введите заголовок заметки: '))
            new_note.append(input('Введите тело заметки: '))
            new_note.append(date_time_now())
            write_end_file(new_note, file_path)
            print('Заметка успешно сохранена')
        elif choice == '2':
            print('Все заметки:')
            show_all(file_path, style_view)

        elif choice == '3':
            user_id = input('Введите id заметки: ')
            print(f'Заметка c id={user_id}:')
            show_note_id(file_path, user_id, style_view)
        elif choice == '4':
            user_id = input('Введите id заметки: ')
            replace_id(file_path, user_id)
        elif choice == '5':
            user_id = input('Введите id заметки: ')
            print(f'Заметка c id={user_id}:')
            del_id(file_path, user_id)
        elif choice == '6':
            user_date = ''
            user_date = input('Введите дату (ГГГГ-ММ-ДД): ')
            print(f'Заметки за {user_date}:')
            show_notes_filter_date(file_path, user_date, style_view)


main()

from typing import NoReturn
import json
import datetime

notes = []

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file)
    print('Заметка сохранена')

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def show_all(filtered_notes=None):
    if not filtered_notes:
        filtered_notes = notes
    for note in filtered_notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Message: {note['body']}, Time: {note['time']}")

def show_One():
    note_id = input('Введите ID заметки: ')
    for note in notes:
        if note['id'] == note_id:
            print(f"ID: {note['id']}, Title: {note['title']}, Message: {note['body']}, Time: {note['time']}")

def delete():
    note_target = input('Введите заголовок заметки: ')
    global notes
    notes = [note for note in notes if note['title'] != note_target]
    save_notes()
def change():
    target_id = input("Введите id или нажмите Enter")
    new_title = input('Введите новый заголовок: ')
    new_body = input('Введите новое сообщение: ')
    new_time = str(datetime.datetime.now())
    if len(target_id) > 0:
        for note in notes:
            if note['id'] == target_id:
                note['title'] = new_title
                note['message'] = new_body
                note['timestamp'] = new_time
                save_notes()
                break
    else:
        target_title = input('Введите искомый заголовок: ')
        for note in notes:
            if note['title'] == target_title:
                note['title'] = new_title
                note['message'] = new_body
                note['timestamp'] = new_time
                save_notes()
                break

def add_new() -> NoReturn:
    id = len(notes) + 1
    title = input('Введите заголовок: ')
    body = input('Введите заметку: ')
    time = str(datetime.datetime.now())
    note = {
        'id': id,
        'title': title,
        'body': body,
        'time': time
    }
    notes.append(note)
    save_notes()

def copy_contacts(file_name_source: str, file_name_destination: str):
    with open(file_name_source, 'r', encoding='utf-8') as fd:
        data_source = fd.readlines()
        fd.close()
    with open(file_name_destination, 'a', encoding='utf-8') as fd:
        index = input("Какую строку желаете перенести?: ")
        fd.write(data_source[int(index)])
        fd.close()

def showWithFilter():
    date = input("Введите дату для фильтрации (гггг-мм-дд): ")
    filtered_notes = [note for note in notes if date in note['timestamp']]
    show_all(filtered_notes)

def main():
    with open('notes.json', 'r') as file:
        global notes
        notes = json.load(file)
    flag_exit = False
    print("Инструкция: ")
    print("x               Выход из программы")
    print("showAll         Показать все заметки ")
    print("showOne         Показать одну заметку")
    print("showWithFilter  Отфильтровать замектки по дате")
    print("add             Добавить новую заметку")
    print("edit            Изменить существующую заметку")
    print("delete          Удалить существующую заметку")
    while not flag_exit:
        answer = input('Введите команду или х для выхода: ')
        if answer == 'x':
            flag_exit = True
            print('До свидания')
        elif answer == 'showAll':
            show_all()
        elif answer == 'showOne':
            show_One()
        elif answer == 'showWithFilter':
            showWithFilter()
        elif answer == 'add':
            add_new()
        elif answer == 'edit':
            change()
        elif answer == 'delete':
            delete()

if __name__ == '__main__':
    main()
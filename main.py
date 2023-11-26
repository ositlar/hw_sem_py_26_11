from typing import NoReturn


def show_all(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as fd:
        contacts = fd.readlines()
        print("".join(contacts))

def remove(file_name: str):
    surname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    target = f'{surname}, {firstname}, {patronymic}, {phone_number}\n'
    with open(file_name, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
        data.remove(target)
        fd.close()
    with open(file_name, 'w', encoding='utf-8') as fd:
        fd.writelines(data)
        fd.close()

def change(file_name: str):
    surname_old = input('Введите фамилию: ')
    firstname_old = input('Введите имя: ')
    patronymic_old = input('Введите отчество: ')
    phone_number_old = input('Введите номер телефона: ')
    target = f'{surname_old}, {firstname_old}, {patronymic_old}, {phone_number_old}\n'
    print("Введите новые данные")
    surname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    new = f'{surname}, {firstname}, {patronymic}, {phone_number}\n'
    with open(file_name, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
        index = data.index(target)
        data[index] = new
        fd.close()
    with open(file_name, 'w', encoding='utf-8') as fd:
        fd.writelines(data)
        fd.close()

def add_new(file_name: str) -> NoReturn:
    # Функция принимает имя файла (file_name: str)
    # Запрашивает у пользователя данные в виде ФИО и номера телефона
    # И сохраняет полученные данные
    # param file_name: str имя файла
    # return: None
    surname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')

    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{surname}, {firstname}, {patronymic}, {phone_number}\n')
        fd.close()

def copy_contacts(file_name_source: str, file_name_destination: str):
    with open(file_name_source, 'r', encoding='utf-8') as fd:
        data_source = fd.readlines()
        fd.close()
    with open(file_name_destination, 'a', encoding='utf-8') as fd:
        index = input("Какую строку желаете перенести?: ")
        fd.write(data_source[int(index)])
        fd.close()



def main():
    flag_exit = False
    file_name = 'phone_book.txt'
    file_name_source = 'phone_book_source.txt'
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить запись')
        print('3 - удалить запись')
        print('4 - изменить запись')
        print('5 - перенести контакт из второй книги')
        answer = input('Введите операцию или x для выхода: ')
        if answer == '1':
            show_all(file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            change(file_name)
        elif answer == '5':
            copy_contacts(file_name_source, file_name)
        elif answer == 'x':
            flag_exit = True

if __name__ == '__main__':
    main()
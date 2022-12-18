import time

def error_input():
    print('Ошибка!')
    print('Пожалуйста введите команду соответствующую пункту меню.')
    time.sleep(1)


def done_message():
    print('Выполнено!')


main_menu = \
    'Выберите пункт меню:\n\
    1. Список контактов\n\
    2. Поиск контакта\n\
    3. Добавить контакт вручную\n\
    4. Изменить контакт\n\
    5. Импорт контактов\n\
    6. Экспорт контактов\n\
    7. Выход'

def show_contacts(data):  # 1 in menu
    if data != []:
        print('Список контактов:')
        for item in range(len(data)):
            a = data[item]['contact_id']
            b = data[item]['surname']
            c = data[item]['name']
            d = data[item]['phone']
            e = data[item]['comment']
            print(f'{a}) {b} {c}. {d}. {e}.')
        print(50 * "•")
    else:
        print('Список контактов пуст')

def start_page():  # Starting page, choose number
    print(main_menu)
    print(50 * "═")
    print()
    command = input('Выберите действие:  ')
    print(50 * "_")
    return command


def search_contact():
    search_request = input('Введите данные для поиска: ')
    print(50 * "=")
    return search_request


def add_contact():
    print('Добавление контакта')
    print(50 * "-")
    contact_surname = input('Введите фамилию ')  # plain text
    contact_name = input('Введите имя ')  # DD-MM-YY
    contact_number = input('Введите номер телефона')
    commentary = input('Комментарий')
    contact = [{'contact_id': '', 'surname': contact_surname, 'name': contact_name, 'phone': contact_number,
                'comment': commentary}, ]
    return contact  # возвращение списка словаря


def change_contact():
    print('Изменить контакт:')
    print(50 * "~")
    contact_id = input('Выберите контакт для внесения изменений: ')
    return int(contact_id)


def change_contact_content(one_contact):
    while True:
        menu_command = input('Что необходимо сделать?\n 1 - Изменить содержание \n 2 - Удалить контакт\n')
        if menu_command == '1':
            print('Изменить содержание контакта:')
            while True:
                submenu_command = input(
                    'Что необходимо изменить?\n 1 - Изменить фамилию \n 2 - Изменить имя\n 3 - Изменить номер телефона\n 4 - Изменить комментарий\n')
                match submenu_command:
                    case '1':  # Изменить фамилию
                        print('Введите фамилию: ')
                        one_contact['surname'] = input()
                        done_message()
                        break
                    case '2':  # Изменить имя
                        print('Введите имя: ')
                        one_contact['name'] = input()
                        done_message()
                        break
                    case '3':  # Изменить номер телефона
                        print('Введите номер телефона: ')
                        one_contact['phone'] = input()
                        done_message()
                        break
                    case '4':  # Изменить комментарий
                        print('Введите комментарий: ')
                        one_contact['comment'] = input()
                        done_message()
                        break
                    case _:
                        error_input()
            break
        elif menu_command == '2':
            one_contact['comment'] = 'Я что-то нажал и всё сломалось'  # удаление по ID
            done_message()
            break
    return one_contact


def bye_mess():  # 6 in menu
    print('Работа завершена!')


def import_contacts():
    print('Импорт контактов:')
    print('Пожалуйста выберите формат файла для импорта:')
    import_type = input('csv\njson\n ')
    return import_type


def export_contacts():
    print('Экспорт контактов:')
    print('Пожалуйста выберите формат файла для экпорта:')
    export_type = input('csv\njson\n')
    return export_type


def result_mess(done):
    if done:
        done_message()
    else:
        print('Произошла ошибка при выполнении операции!')
import csv
from termcolor import colored, cprint


# Функция вывода Фио, телефонов, описаний из csv файла
def show(x: int):
    """
    :param x: Цифра от 1 до 3
    :return: Ничего не возвращает, а просто выводит на печать ФИО, Телефон или Описание в
    зависимости от x
    """
    if x == 1:
        def name():
            with open('phone_book.csv', 'r') as f:
                reader = csv.reader(f)
                list2 = [row.split(";")[0:3] for row in f]
                for count, list in enumerate(list2):
                    print(count, "".join([str(_) for _ in list]))

        name()
    elif x == 2:
        def number():
            with open('phone_book.csv', 'r') as f:
                reader = csv.reader(f)
                list2 = [row.split(";")[3] for row in f]
                for count, list in enumerate(list2):
                    print(count, list)

        number()
    elif x == 3:
        def description():
            with open('phone_book.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                list2 = [row.split(";")[4].replace('\n', '') for row in f]
                for count, list in enumerate(list2):
                    print(count, list)

        description()


# Добавляет в телефонную книгу человека, а также возвращает список из Ф И Т О
def add_person():
    name = input('Введите полное ФИО человека через пробел: ').split(' ')
    number = input('Введите № телефона: ')
    description = input('Введите описание: ')
    with open('phone_book.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([name[0], name[1], name[2], number, description])
    return [name[0], name[1], name[2], number, description]


# Удаляет человека из телефонной книги 'phone_book.csv' по номеру
def edit_phone_book():
    action = input(
        f'Вы хотите {colored("удалить - 1", "red")} или {colored("отредактировать данные - 2", "green")}:    ')
    if action in '1':
        with open('phone_book.csv', 'r') as f:
            l = f.readlines()
        record_number = int(input("Введите цифру кого вы хотите удалить: "))
        l[record_number - 1] = ''
        with open('phone_book.csv', 'w') as f:
            f.writelines(l)
    else:
        action = input(colored(f'Что вы хотите отредактировать ? {colored("ФИО - 1", "red")} | '
                               f'{colored("Номер - 2", "green")} |'
                               f' {colored("Описание - 3", "blue")}'))

        with open('phone_book.csv', 'r') as f:
            reader = csv.reader(f)
        # edit name
        if action in '1':
            print(show(1))
            action = int(input(f'Введите цифру кого вы хотите изменить ?'))
            new_record = input('Введите новое значение ФИО через пробел: ').split(' ')
            with open('phone_book.csv', 'r', newline='') as read_obj:
                csv_reader = csv.reader(read_obj)
                list_of_csv = list(csv_reader)
                correct_lst = list_of_csv[action][0].replace(';', '').split()
                print(correct_lst)
                correct_lst[0], correct_lst[1], correct_lst[2] = new_record[0], new_record[1], new_record[2]
                print(f'ФИО {colored("изменено", "red")}', correct_lst)  # У нас теперь есть лист для записи в файл
                # Нужно старую запись убрать
                with open('phone_book.csv', 'r') as f:
                    l = f.readlines()
                l[action] = ''
                with open('phone_book.csv', 'w') as f:
                    f.writelines(l)
                # Добавить новую
                with open('phone_book.csv', 'a+', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow([correct_lst[0], correct_lst[1], correct_lst[2], correct_lst[3], correct_lst[4]])
        # edit number
        elif action in '2':
            show(2)
            action = int(input(f'Введите цифру номера телефона который хотите изменить ?'))
            new_record = input('Введите новое значение телефона: ')
            with open('phone_book.csv', 'r', newline='') as read_obj:
                csv_reader = csv.reader(read_obj)
                list_of_csv = list(csv_reader)
                correct_lst = list_of_csv[action][0].replace(';', '').split()
                correct_lst[3] = new_record
                print(f'Номер телефон{colored("изменен", "red")}', correct_lst)
            # Нужно старую запись убрать
            with open('phone_book.csv', 'r') as f:
                l = f.readlines()
            l[action] = ''
            with open('phone_book.csv', 'w') as f:
                f.writelines(l)
            # Добавить новую
            with open('phone_book.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([correct_lst[0], correct_lst[1], correct_lst[2], correct_lst[3], correct_lst[4]])
        # edit description
        elif action in '3':
            show(3)
            action = int(input(f'Введите цифру кого вы хотите изменить ?'))
            new_record = input('Введите новое описание: ')
            with open('phone_book.csv', 'r', newline='') as read_obj:
                csv_reader = csv.reader(read_obj)
                list_of_csv = list(csv_reader)
                correct_lst = list_of_csv[action][0].replace(';', '').split()
                correct_lst[4] = new_record
                print(f'Описание {colored("изменено", "red")}', correct_lst)
            # Нужно старую запись убрать
            with open('phone_book.csv', 'r') as f:
                l = f.readlines()
            l[action] = ''
            with open('phone_book.csv', 'w') as f:
                f.writelines(l)
            # Добавить новую
            with open('phone_book.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([correct_lst[0], correct_lst[1], correct_lst[2], correct_lst[3], correct_lst[4]])

            pass

    # log(f'Удалена запись ...')# Возможно будет логирование, это задел на будущее
edit_phone_book()

# Из готового файла происходит чтение и затем вывод на печать по требованию
def read_phone_book():
    all_csv = colored('Весь', 'red', attrs=['underline'])
    column = colored('Колонку', 'green', attrs=['underline'])
    x = int(input(f'Вы хотите посмотреть {all_csv} тел. справочник или какую-то {column}?'
                  f'\n{all_csv} - 1 | {column} - 2:    '))
    if x == 2:
        question = int(input('\nКакую колонку вы хотите просмотреть?\n'
                         f'{colored("ФИО - 1", "red")} | {colored("Телефон - 2", "green")} '
                         f'| {colored("Описание - 3", "blue")}:    '))
        if question == 1:
            show(1)
            pass
        elif question == 2:
            show(2)
            pass
        elif question == 3:
            show(3)
            pass
    else:
        file = open("phone_book.csv", "r")
        print(file.read())  # Просто выводит на печать весь file
        # print(f.readlines()) # Возвращает список с разделителем ;


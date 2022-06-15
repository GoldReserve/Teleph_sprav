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
                    print(count,
                          " ".join([str(_) for _ in list]))  # TODO оставить на рефакторинг ровный вывод имен в консоль

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
    elif x == 4:
        def all_row():
            with open('phone_book.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                list2 = [row[0:].replace(';', ' ').replace('\n', '') for row in f]
                for count, list in enumerate(list2):
                    print(count, list)
        all_row()



# Добавляет в телефонную книгу человека, а также возвращает список из Ф И Т О
# TODO 1. реализовать чтобы принимала от Дениса лист и записывала затем в csv from_list_to_csv и
# TODO 2.from_csv_to_list Две функии одна от дениса берет лист загоняет в csv и вторая из csv переводит в list и передает Денису для экспорта
def add_person():
    name = input('Введите полное ФИО человека через пробел: ').split(' ')
    number = input('Введите № телефона: ')
    description = input('Введите описание: ')
    with open('phone_book.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([name[0], name[1], name[2], number, description])
    return [name[0], name[1], name[2], number, description]





# Удаляет человека из телефонной книги 'phone_book.csv' по номеру
# TODO 1. Сделать подфункцию(чтение,изменение,удаление,добавление) чтобы не дублировать куски кода в if,elif,elif
# TODO 2. Добавить всю строку которую редактируешь
def edit_phone_book():
    action = input(
        f'Вы хотите {colored("удалить - 1", "red")} или {colored("отредактировать данные - 2", "green")}:    ')
    if action in '1':
        with open('phone_book.csv', 'r') as f:
            line = f.readlines()
        show(1)
        record_number = int(input("Введите цифру кого вы хотите удалить: "))
        line[record_number] = ''
        with open('phone_book.csv', 'w') as f:
            f.writelines(line)
    else:
        action = input(colored(f'Что вы хотите отредактировать ? {colored("ФИО - 1", "red")} | '
                               f'{colored("Номер - 2", "green")} |'
                               f' {colored("Описание - 3", "blue")}:    '))

        # with open('phone_book.csv', 'r') as f:
        #     reader = csv.reader(f)
        if action in '1':
            print(show(4))
            action = int(input(f'Введите цифру кого вы хотите изменить ?'))
            new_record = input('Введите новое значение ФИО через пробел: ').split(' ')
            with open('phone_book.csv', 'r', newline='') as read_obj:
                csv_reader = csv.reader(read_obj)
                list_of_csv = list(csv_reader)
                correct_lst = list_of_csv[action][0].split(";")
                print(correct_lst)
                correct_lst[0], correct_lst[1], correct_lst[2] = new_record[0], new_record[1], new_record[2]
                print(f'ФИО {colored("изменено", "red")}', correct_lst)
                with open('phone_book.csv', 'r') as f:
                    line = f.readlines()
                line[action] = ''
                with open('phone_book.csv', 'w') as f:
                    f.writelines(line)
                with open('phone_book.csv', 'a+', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow([correct_lst[0], correct_lst[1], correct_lst[2], correct_lst[3], correct_lst[4]])
        elif action in '2':
            show(2)
            action = int(input(f'Введите цифру номера телефона который хотите изменить ?'))
            new_record = input('Введите новое значение телефона: ')
            with open('phone_book.csv', 'r', newline='') as read_obj:
                csv_reader = csv.reader(read_obj)
                list_of_csv = list(csv_reader)
                correct_lst = list_of_csv[action][0].replace(';', '').split()
                # print(correct_lst) #ПРОВЕРКА
                correct_lst[
                    3] = new_record  # OUT OF RANGE если не в том формате записано потому что split не корректно работает
                print(f'Номер телефон{colored("изменен", "red")}', correct_lst)
            with open('phone_book.csv', 'r') as f:
                line = f.readlines()
            line[action] = ''
            with open('phone_book.csv', 'w') as f:
                f.writelines(line)
            with open('phone_book.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([correct_lst[0], correct_lst[1], correct_lst[2], correct_lst[3], correct_lst[4]])
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
            with open('phone_book.csv', 'r') as f:
                line = f.readlines()
            line[action] = ''
            with open('phone_book.csv', 'w') as f:
                f.writelines(line)
            with open('phone_book.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([correct_lst[0], correct_lst[1], correct_lst[2], correct_lst[3], correct_lst[4]])

# edit_phone_book()
# Из готового файла происходит чтение и затем вывод на печать
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
        print(file.read().replace(';', ' '))  # Просто выводит на печать весь file
        # print(f.readlines()) # Возвращает список с разделителем ;


# add_person()
# read_phone_book()
# edit_phone_book()

lst = [["Иванов;Иван;Иванович;89163678796;Коллега"], ["Петров;Петр;Петрович;89173217896;Сосед"],
       ["Евгеньев;Евгений;Евгеньевич;89263645789;Сват"], ["Александров;Александр;Александрович;89143214586;Брат"],
       ["Сергеев;Сергей;Сергеевич;89636541896;Папа"], ["Антонова;Антонина;Антоновна;89356789451;Мама"]]

def add_persons(x: list):
    """
    :param x: Денис передает list из листов с людьми
    :return: ---
    """
    with open('phone_book.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for count, people in enumerate(x):
            writer.writerow(x[count][0].split(';'))


# add_persons(lst)

def csv_to_list():
    with open('phone_book.csv', 'r') as f:
        line = f.readlines()
        lst = []
        for elem in line:
            lst.append(elem.strip().split(";"))
    return lst


print(csv_to_list())

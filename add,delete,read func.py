import csv


# Добавляет в телефонную книгу человека, а также возвращает список из Ф И Т О 
def add_task():
    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    number = input('Введите № телефона: ')
    description = input('Введите описание: ')
    with open('phone_book.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([surname, name, number, description])
    return [surname, name, number, description]

# Удаляет человека из телефонной книги 'phone_book.csv' по номеру
def delete_person(record_number: int):
    """
    :param record_number: Чтобы удалить 15 запись передать 15
    :return: Ничего, просто удаляет нужную нам строчку из csv файла
    """
    with open('phone_book.csv', 'r') as f:
        l = f.readlines()
    l[record_number - 1] = ''
    with open('phone_book.csv', 'w') as f:
        f.writelines(l)
    # log(f'Удалена запись ...')# Возможно будет логирование, это задел на будущее

# Из готового файла происходит чтение и затем вывод на печать по требованию
def read_phone_book():
        file = open("phone_book.csv", "r")
        print(file.read()) # Просто выводит на печать весь file
        # print(f.readlines()) # Возвращает список с разделителем ;

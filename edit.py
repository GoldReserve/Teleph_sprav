# l = [
#     ['Фамилия1', 'Имя1', '555-66-777', 'Друг'],
#     ['Фамилия2', 'Имя2', '777-66-777', 'Друг'],
#     ['Фамилия3', 'Имя3', '666-66-777', 'Коллега'],
#     ['Фамилия4 Слишком длинная фамилия', 'Имя4', '333-66-777', 'Брат'],
#     ['Фамилия5', 'Имя5', '222-66-777', 'Друг'],
# ]
# l = []


def edit_contact(contacts: list) -> list:
    """Редактирование контакта
    если введено не число -> ошибка ввода -> list
    если контакт не найден -> контакт не найден -> list
    :return: list
    """
    if not contacts:
        print("\033[41mСписок контактов пуст!\033[0m")
        return contacts
    try:
        id_cont = int(input("Номер контакта для редактирования: "))
    except ValueError:
        print("Ошибка ввода")
        return contacts
    tmp = ""
    no_contact = True
    for key, value in enumerate(contacts):
        if id_cont == key:
            no_contact = False
            for i in range(len(value)):
                tmp = value[i]
                value[i] = input(f"Старое значение \033[32m'{value[i]:15}\033[0m',"
                                 f" введите новое "
                                 f"\033[033m(Enter=оставить как есть):\033[0m").strip()
                if value[i] == '':
                    value[i] = tmp
    if no_contact:
        print("Нет такого контакта")
        return contacts
    # print(contacts)
    return contacts


# edit_contact(l)

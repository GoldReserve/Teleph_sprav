def edit_contact(contacts: list):
    id_cont = int(input("Номер контакта для редактирования: "))
    for k, v in enumerate(contacts):
        if id_cont == k:
            v[0] = input(f"старый номер='{v[0]}', новый номер: ")
            v[1] = input(f"Редактировать '{v[1]}' : ")
            v[2] = input(f"Редактировать '{v[2]}', новое описание: ")
    print(contacts)
    return contacts

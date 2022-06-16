from import_export import import_file
import add_delete_read_func
def menu():

    def menu_interface():
        list_menu = ['1. Показать телефонную книгу', '2. Добавить контакт', '3. Редактировать контакт',
                     '4. Удалить контакт', '5. Импортировать контакт', '6. Выход']
        len_id_menu = len(list_menu[0])
        for i in list_menu:
            if len_id_menu < len(i):
                len_id_menu = len(i)
        len_id_menu += 9
        print('\t Меню телефонного справочника \t')
        print('=' * len_id_menu)
        for i in list_menu:
            print(f'+  {i}')
        print('=' * len_id_menu)
        print('')
        return list_menu

    res = 0
    while res != 6:
        l_menu = menu_interface()
        id_menu = 0
        count_of_points_menu = len(l_menu) # Пусть количество пунктов будет в отдельной переменной.
        id_menu = input(f'Выберите пункт меню (1-{len(l_menu)}): ')
        if id_menu.isdigit():  # Проверка на цифры
            if int(id_menu) > 0 and int(id_menu) < count_of_points_menu + 1: res = -1  # Проверка на диапазон пунктов
            match  id_menu:
                case '1': print(1)
                case '2': 
                    print('++++++++++++++++++++++++++')
                    print('Список ваших текущих задач')
                    print('++++++++++++++++++++++++++')
                
                    print('++++++++++++++++++++++++++')
                case '3':
                    print('++++++++++++++++++++++++++')
                    print('Редактирование записи')
                    print('++++++++++++++++++++++++++')

                case '4': 
                    print('++++++++++++++++++++++++++')
                    print('Список ваших завершенных задач')
                    print('++++++++++++++++++++++++++')
                
                    print('++++++++++++++++++++++++++')
                case '5': 
                    print('++++++++++++++++++++++++++')
                    print('Импорт контактов')
                    print('++++++++++++++++++++++++++')
                    import_file()
                case '6': break
        else:
            print("Введите пожалуйста число (арабское), и нажмите клавишу 'Enter'!")
    return exit

menu()
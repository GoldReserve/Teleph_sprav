def impexp_file(list_in):
    import os.path
    
    # Функция вывода на экран импортированных данных - Удалить при слиянии
    def show_all(lst):
        for item in lst:
            print(f'|| {item[0][:15]:15} | {item[1]:15} | {item[2]:10} | {item[3]:10}')

    print('Импорт/Экспорт файла контактов')
    file_exist = False
    while file_exist != True:
        in_put = input('Импорт - 1 | Экспорт -2 | Выход - 3 \t (1-3):')
        if in_put == '3': return # Выход из модуля
        
        # Раздел обработки импорта файла
        if in_put == '1':
            import_file = input(f'Введите имя файла для импорта: \t')
            file_exist = os.path.exists(import_file)  # Проверка на существование файла
            if file_exist == True: 
                print(f'{import_file} - файл найден...')
                print('Чтение файла')                              # - Удалить при слиянии
                # import_file = from_csv_to_list(import_file)    # Получаем данные из файла
                import_file = [['Ахметдянов','Ахмет','+79800000001','комит т1'],['Буржуев','Буржуй','+79800000002','комит т2']] # - Удалить при слиянии
                show_all(import_file)                        # Показать пользователю импортированные данные
                y_n = input(f'Выполнить импорт? (y/n): \t')
                if y_n == 'y': 
                    list_in += import_file
                    print('Запись файла')                           # - Удалить при слиянии
                    #from_list_to_csv(list_in, 0)  # Записываем данные в файл (если 0 - то файл по умолчанию, иначе указанный файл)
            elif file_exist == False: print('Файл отсутствует!') # Возврат в меню модуля
        
        # Раздел обработки экспорта в файл
        if in_put == '2':
            export_file = input(f'Введите имя файла для экспорта: \t')
            file_exist = os.path.exists(export_file)  # Проверка на существование файла
            if file_exist == True: 
                print(f'{export_file} - файл существует! Перезаписать? (y/n): \t')
                if y_n == 'y': 
                    print('Запись файла')                           # - Удалить при слиянии
                    #from_list_to_csv(list_in, export_file)  # # Записываем данные вуказанный  файл (если 0 - то файл по умолчанию)
            elif file_exist == False:
                print('Запись файла')                               # - Удалить при слиянии
                file_exist = True
                #from_list_to_csv(list_in, export_file)  # # Записываем данные вуказанный  файл (если 0 - то файл по умолчанию)
        

List_In = [['Иванов', 'Иван', '+79260000001','комментарий 1'], ['Петров', 'Петр', '+79260000002','комментарий 2'], ['Васильев', 'Василий', '+79260000003','комментарий 3'] ] # - Удалить при слиянии
impexp_file(List_In)       

def import_file():
    import csv
    import os.path

    print('Модуль импорта файла')
    file_ex = input(f'Введите имя файла для импорта: \t')
    file_exist = os.path.exists(file_ex)
    if file_exist == False:
        print(f'{file_ex} не существует !!!')
        return 0
    else:
        with open(file_ex, 'r') as file:
            reader = list(csv.reader(file))
            print(f'Содержимое файла:')
            for i in reader:
                index = reader.index(i)
                reader[index] = str(i)[2:-2]
                row = reader[index].split(';')
                print(f'{row[0]} \t {row[1]} \t {row[2]}')
        import_f = (f'Импортируем? (y/n): \t')
        if import_f == 'y':
            return list(reader)

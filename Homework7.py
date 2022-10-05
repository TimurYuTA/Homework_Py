# Задача 1 - TXT
# Создать телефонный справочник с возможностью импорта и экспорта данных формате .txt.

# def data_import():
#     FIO = input('\nЗаполните даннные нового контакта:\nВведите ФИО: ').upper()
#     phone = input('Введите номер телефона используя только цифры: ')
#     while phone.isdigit() == False:
#         phone = input('Ошибка! Введите номер телефона используя только цифры: ')
#     comment = input('Напишите комментарий: ').lower()
#     with open('Phonebook.txt', 'a', encoding='utf-8') as book:
#         book.write(f'ФИО: {FIO}\tтел.: {phone} - {comment}\n')
#     print('\nКонтакт добавлен!\n')

# def data_export():
#     with open('Phonebook.txt', 'r', encoding='utf-8') as book:
#         data = book.readlines()
#     action_find = int(input('\nВыберите критерий для поиска контакта:\n1 - ФИО\n2 - Номер телефона\nВведите номер критерия: '))
#     while action_find < 1 or action_find > 2:
#         action_find = int(input('Вы ошиблись! Введите номер критерия (1 или 2): '))
#     count_find = 0
#     if action_find == 1:
#         data_find = input('\nВведите ФИО контакта: ').upper()
#     elif action_find == 2:
#         data_find = input('\nВведите номер телефона контакта используя только цифры: ')
#         while data_find.isdigit() == False:
#             data_find = input('Вы ошиблись! Введите номер телефона контакта используя только цифры: ')
#     print('\nРезультаты поиска по вашему запросу:\n')
#     for line in data:
#         if data_find in line:
#             count_find += 1
#             print(f'{count_find}. {line}')
#     if count_find == 0:
#         print('Контакт не найден!\n')


# flag = True
# while flag == True:
#     operation = int(input('\nВыберите действие:\n1 - Импорт контакта\n2 - Экспорт контакта\n3 - Выход из программы\nВведите номер выбранного действия: '))
#     if operation == 1: data_import()
#     elif operation == 2: data_export()
#     elif operation == 3:
#         print('\nВы вышли из программы!\n') 
#         flag = False
#     else: print(f'\nДействия "{operation}" не существует!')



# Задача 1 - CSV

# import csv

# def data_import():
#     add = []
#     print('\nЗаполните даннные нового контакта:')
#     add.append(input('\nВведите Фамилию: ').upper())
#     add.append(input('Введите Имя: ').upper())
#     add.append(input('Введите Отчество: ').upper())
#     phone = input('Введите номер телефона используя только цифры: ')
#     while phone.isdigit() == False:
#         phone = input('Ошибка! Введите номер телефона используя только цифры: ')
#     add.append(phone)
#     add.append(input('Напишите комментарий: ').lower())
#     with open('Phonebook.csv', 'a', encoding='utf-8') as book:
#         new_contact = csv.writer(book, delimiter = ' ', lineterminator='\n')
#         new_contact.writerow(add)
#     print('\nКонтакт добавлен!\n')

# def data_export():
#     with open('Phonebook.csv', 'r', encoding='utf-8') as book:
#         data = list(csv.reader(book, delimiter = ' '))
#     action_find = int(input('\nВыберите критерий для поиска контакта:\n1 - ФИО\n2 - Номер телефона\nВведите номер критерия: '))
#     while action_find < 1 or action_find > 2:
#         action_find = int(input('\nВы ошиблись! Введите номер критерия (1 или 2): '))
#     count_find = 0
#     if action_find == 1:
#         data_find = []
#         data_find.append(input('\nВведите Фамилию контакта: ').upper())
#         data_find.append(input('Введите Имя контакта: ').upper())
#         data_find.append(input('Введите Отчество контакта: ').upper())
#         print('\nРезультаты поиска по вашему запросу:')
#         for i in data:
#             coincidences = 0
#             for j in range(3):
#                 if data_find[j] == '' or data_find[j] == '-':
#                     coincidences += 1
#                 elif data_find[j] == i[j]:
#                     coincidences += 1
#             if coincidences == 3:
#                 count_find += 1
#                 find_export = ' '.join(i)
#                 print(f'{count_find}. {find_export}')
#     elif action_find == 2:
#         data_find = input('\nВведите номер телефона контакта используя только цифры: ')
#         while data_find.isdigit() == False:
#             data_find = input('Вы ошиблись!\nВведите номер телефона контакта используя только цифры: ')
#         print('\nРезультаты поиска по вашему запросу:')
#         for i in data:
#             if data_find == i[3]:
#                 count_find += 1
#                 find_export = ' '.join(i)
#                 print(f'{count_find}. {find_export}')
#     if count_find == 0:
#             print('Контакт не найден!\n')


# flag = True
# while flag == True:
#     operation = int(input('\nВыберите действие:\n1 - Импорт контакта\n2 - Экспорт контакта\n3 - Выход из программы\nВведите номер выбранного действия: '))
#     if operation == 1: data_import()
#     elif operation == 2: data_export()
#     elif operation == 3:
#         print('\nВы вышли из программы!\n') 
#         flag = False
#     else: print(f'\nДействия "{operation}" не существует!')

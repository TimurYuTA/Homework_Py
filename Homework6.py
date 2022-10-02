# Задача 1.
# Написать функцию print_operation_table(operation, num_rows, num_columns)

# def summ(x, y):
#     return (x + y)

# def subtraction(x, y):
#     return (x - y)

# def multiplication(x, y):
#     return (x * y)

# def division(x, y):
#     return (x / y)

# def print_operation_table(operation, num_rows, num_columns):
#     for i in range(1, num_rows + 1):
#         row_list = []
#         for j in range(1, num_columns + 1):
#             row_list.append(str(operation(i, j)))
#         print('\t'.join(row_list))


# rows = int(input('Введите количество строк: '))
# columns = int(input('Введите количество столбцов: '))
# operat = int(input('Выберите действие (1 - сумма, 2 - вычитание, 3 - умножение, 4 - деление): '))
# while operat < 1 or operat > 4:
#     operat = int(input('Ошибка! Введите одно значение от 1 до 4!\nВыберите действие (1 - сумма, 2 - вычитание, 3 - умножение, 4 - деление): '))
# if operat == 1: print_operation_table(summ, rows, columns)
# elif operat == 2: print_operation_table(subtraction, rows, columns)
# elif operat == 3: print_operation_table(multiplication, rows, columns)
# elif operat == 4: print_operation_table(division, rows, columns)



# Задача 2.
# Мимикрия

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 'asd']
# transformed_values = list(map(transformation, values))
# if values == transformed_values: print('Ok')
# else: print('fail')



# Задача 3.
# Самая далёкая планета

# def find_farthest_orbit(list_of_orbits):
#     s_max_orbit = 0
#     max_orbit = ''
#     for i in list_of_orbits:
#         if i[0] != i[1]:
#             if (3.14 * i[0] * i[1]) > s_max_orbit:
#                 s_max_orbit = 3.14 * i[0] * i[1]
#                 max_orbit = i
#     return max_orbit


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))



# Задача 4.
# Пам-парам парам-пам парам

# krichalka = input('Винни, напиши кричалку: ').lower().split()
# krichalka[0].count('а')
# for i in krichalka:
#     if krichalka[0].count('а') != i.count('а'):
#         print('Пам парам')
#         exit()
# print('\nПарам пам-пам\n')



# Задача 5.
# Все равны, как на подбор

# def same_by(characteristic, objects):
#     if sum(list(map(characteristic, objects))) == 0:
#         return True
#     else:
#         return False


# values = []
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# Суперсдвиг - ДЗ-3 (ДОП)! Не заметил её когда решал ДЗ-3, поэтому решил тут)
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

# n = int(input('\nВведите количество чисел в последовательности: '))
# List_in = [int(input(f'Введите {i + 1}-е число: ')) for i in range(n)]
# k = int(input('\nЗадайте сдвиг: '))
# print(f'\n{List_in} - без сдвига')
# if k > 0:
#     for i in range(k % n):
#         List_in.insert(0, List_in[n - 1])
#         List_in.pop()
# elif k < 0:
#     for i in range((k * (-1)) % n):
#         List_in.append(List_in[0])
#         List_in.pop(0)
# print(f'{List_in} - со сдвигом\n')



# Задача 1.
# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь (БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

# n = int(input('\nЗадайте точность (количество знаков после запятой): '))
# pi = (1 / (16 ** 0)) * (4 / (8 * 0 + 1) - 2 / (8 * 0 + 4) - 1 / (8 * 0 + 5) - 1 / (8 * 0 + 6))
# for i in range(1, n + 1):
#     pi += (1 / (16 ** i)) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
# print(f'\nЧисло Пи с точночть {n} знаков после запятой -> {round(pi, n)}\n')



# Задача 2.
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('\nВведите натуральное число N: '))
# list_n = []
# i = 2
# while n > 1:
#     if n % i == 0:
#         list_n.append(i)
#         n = n / i 
#     else: i += 1
# print(f'\nСписок простых множителей вашего числа  -> {list_n}\n')



# Задача 3.
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

# n = int(input('\nЗадайте количество чисел в последовательности: '))
# list_in = [int(input(f'Введите {i + 1}-е число: ')) for i in range(n)]
# list_out = []
# i = 0
# while i < n:
#     if list_in[i] in list_out: i += 1
#     else: 
#         list_out.append(list_in[i])
#         i += 1
# print(f'\n{list_in} -> {list_out}\n')



# Задача 4.
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint


# k = int(input('\nВведите натуральную степень k: '))
# list_m = []
# for i in range(0, k + 1):
#     number = randint(0, 100)
#     if number != 0:
#         if number == 1:
#             if i == 0: list_m.insert(0, str(number))
#             elif i == 1: list_m.insert(0, 'x')
#             else: list_m.insert(0, 'x^' + str(i))
#         else:
#             if i == 0: list_m.insert(0, str(number))
#             elif i == 1: list_m.insert(0, str(number) + '*x')
#             else: list_m.insert(0, str(number) + '*x^' + str(i))
# str_m = ' + '.join(list_m) + ' = 0'
# with open('4-4.txt', 'w') as f: f.write(str_m)
# print(f'\n{str_m}\n')



# Задача 5.
# 35. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from random import randint
import re

for j in range(2):   # Создаём два файла, в каждый из которых создаем и записываем многочлен
    k = int(input('\nВведите натуральную степень k: '))
    list_m = []
    for i in range(0, k + 1):
        number = randint(0, 100)
        if number != 0:
            if number == 1:
                if i == 0: list_m.insert(0, str(number))
                elif i == 1: list_m.insert(0, 'x')
                else: list_m.insert(0, 'x^' + str(i))
            else:
                if i == 0: list_m.insert(0, str(number))
                elif i == 1: list_m.insert(0, str(number) + '*x1')
                else: list_m.insert(0, str(number) + '*x^' + str(i))
    str_m = ' + '.join(list_m) + ' = 0'
    with open(f'4-5-{j + 1}.txt', 'w') as file: file.write(str_m)

with open('4-5-1.txt', 'r') as file_1: list_1 = file_1.read()[:-4].split(' + ')
with open('4-5-2.txt', 'r') as file_2: list_2 = file_2.read()[:-4].split(' + ')

power = max(int(list_1[0].split('*x^')[1]), int(list_2[0].split('*x^')[1]))
list_sum = []
# for i in range(power, 0, -1):
#     if 
print(power)




# Задача 6.
# (Дополнительная задача) https://www.eolymp.com/ru/problems/854

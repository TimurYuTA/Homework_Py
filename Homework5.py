# Задача 1.
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def Kosti():
    res = randint(1, 6)
    return res

# Вводные данные для игры:
n = 221  # Количество конфет в игре
min_n = 1  # минимальное количество конфет за ход
max_n = 28  # максимальное количество конфет за ход

# Определяем игроков + жеребьёвка
print('\nИграют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.')
print(f'На столе лежит {n} конфет. За один ход можно забрать не более чем {max_n} конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход!')
Player_1 = input('\nВведите имя 1-го игрока: ')
print('\nЕсли хотите сыграть с простым ботом, введите имя 2-го игрока - Bot')
print('Если хотите сыграть с интеллектуальным ботом, введите имя 2-го игрока - sBot')
Player_2 = input('Введите имя 2-го игрока: ')
print(f'\nИтак, {Player_1} против {Player_2}! Поехали!\n')
print('Давайте бросим кости. У кого сумма значений будет больше, тот ходит первым!')
print('Введите "да" для броска! Либо "нет" для завершения игры!')
sum_1 = 0
sum_2 = 0
while sum_1 == sum_2:
    answer_1 = input(f'\n{Player_1}, бросаем?: ')
    if answer_1.lower() in ' да ':
        brosok_1 = Kosti()
        brosok_2 = Kosti()
        sum_1 = brosok_1 + brosok_2
        print('\nЖребий брошен!')
        print(f'{Player_1}: {brosok_1} и {brosok_2} -> {sum_1}')
    else: 
        print(f'\nИгра окончена! Победитель - {Player_2}!\n')
        exit()
    if Player_2.lower() in ' bot ':
        Player_2 = 'Bot'
        answer_2 = 'да'
    elif Player_2.lower() in ' sbot ':
        Player_2 = 'sBot'
        answer_2 = 'да'
    else:
        answer_2 = input(f'{Player_2}, бросаем?: ')
    if answer_2.lower() in ' да ':
        brosok_1 = Kosti()
        brosok_2 = Kosti()
        sum_2 = brosok_1 + brosok_2
        print(f'{Player_2}: {brosok_1} и {brosok_2} -> {sum_2}')
    else: 
        print(f'\nИгра окончена! Победитель - {Player_1}!\n')
        exit()
if sum_1 > sum_2: 
    first = Player_1
    second = Player_2
    print(f'\nНачинает игру {Player_1}!')
else:
    first = Player_2
    second = Player_1
    print(f'\nНачинает игру {Player_2}!')

# Игра
ostatok = n
while ostatok > 0:
    print(f'\nОсталось {ostatok} конфет!')
    if first == 'Bot':
        if ostatok <= max_n: minus_1 = ostatok
        else: minus_1 = randint(min_n, max_n)
        print(f'Bot взял {minus_1} конфет')
    elif first == 'sBot':
        if ostatok <= max_n: minus_1 = ostatok
        else: minus_1 = ostatok % (max_n + 1)
        print(f'sBot взял {minus_1} конфет')
    else: 
        minus_1 = int(input(f'{first}, сколько возьмёшь? '))
        while minus_1 < min_n or minus_1 > max_n or minus_1 > ostatok:
            print(f'Взять нужно от {min_n} до {max_n} конфет и не больше остатка!')
            minus_1 = int(input(f'{first}, сколько возьмёшь? '))
    ostatok = ostatok - minus_1
    print(f'\nОсталось {ostatok} конфет!')
    if ostatok == 0:
        print(f'\nИгра окончена! Победитель - {first}!\n')
        exit()
    if second == 'Bot':
        if ostatok <= max_n: minus_2 = ostatok
        else: minus_2 = randint(min_n, max_n)
        print(f'Bot взял {minus_2} конфет')
    elif second == 'sBot':
        if ostatok <= max_n: minus_2 = ostatok
        else: minus_2 = ostatok % (max_n + 1)
        print(f'sBot взял {minus_2} конфет')
    else:
        minus_2 = int(input(f'{second}, сколько возьмёшь? '))
        while minus_2 < min_n or minus_2 > max_n or minus_2 > ostatok:
            print(f'Взять нужно от {min_n} до {max_n} конфет и не больше остатка!')
            minus_2 = int(input(f'{second}, сколько возьмёшь? '))
    ostatok = ostatok - minus_2
    if ostatok == 0:
        print(f'\nОсталось {ostatok} конфет!')
        print(f'\nИгра окончена! Победитель - {second}!\n')
        exit()



# Задача 2.
# Создайте программу для игры в ""Крестики-нолики"".



# Задача 3.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
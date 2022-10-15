# Задача 1.
# Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)

# Задача 2.
# Создайте программу для игры с конфетами человек против бота (интелект) (Дополнительно)

# Задача 3.
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, 
# добавив в неё систему логирования (Дополнительно)


# Решение 3 в 1:

# import telebot
# from telebot import types
# from random import randint
# import time


# bot = telebot.TeleBot(token='')


# # Приветствие - команда /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     hello = f'Привет, <b>{message.from_user.first_name}!</b>'
#     bot.send_message(message.chat.id, hello, parse_mode='html')
#     bot.send_message(message.chat.id, 'Для решения задачек необходимо вызвать меню - /menu', parse_mode='html')


# # Меню с кнопками ввода - команда /menu
# @bot.message_handler(commands=['menu'])
# def menu(message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
#     ABV = types.KeyboardButton('Задача № 1 - Удаление слов с "абв"')
#     candies = types.KeyboardButton('Задача № 2 - "Игра с конфетами"')
#     calculator = types.KeyboardButton('Задача № 3 - "Калькулятор"')
#     markup.add(ABV, candies, calculator)
#     answer = bot.send_message(message.chat.id, '<b>Выберите задачу:</b>', parse_mode='html', reply_markup=markup)
#     bot.register_next_step_handler(answer, action)


# # Распределение по задачам
# def action(message):
#     if message.text == 'Задача № 1 - Удаление слов с "абв"':
#         text = bot.send_message(message.chat.id, '<b>Введите текст, а я удалю из него все слова содерщащие сочетание "абв":</b>', parse_mode='html')
#         bot.register_next_step_handler(text, abv)
#     elif message.text == 'Задача № 2 - "Игра с конфетами"':
#         candies_game(message)
#     elif message.text == 'Задача № 3 - "Калькулятор"':
#         calculator(message)


# # Выдача сообщения о завершении задачи
# def end_message(message):
#     bot.send_message(message.chat.id, '<b>Задача завершена!</b>\nДля выбора новой задачи введите - /menu', parse_mode='html')


# # Удаление из текста всех слов, содержащих "абв"
# def abv(message):
#     text_in = message.text.split()
#     text_out = ''
#     count_abv = 0
#     for i in range(len(text_in)):
#         if 'абв' not in text_in[i].lower():
#             if count_abv == 0: 
#                 text_out = text_in[i]
#             else: 
#                 text_out = text_out + ' ' + text_in[i]
#             count_abv += 1
#     bot.send_message(message.chat.id, f'Удалено слов содержащих "абв" - {len(text_in) - count_abv}\nРезультат:')
#     bot.send_message(message.chat.id, f'<b>{text_out}</b>', parse_mode='html')
#     end_message(message)


# # Игра с конфетами (User - Bot)
# # Вводные данные для игры с конфетами:
# n = 221  # Количество конфет в игре
# min_n = 1  # минимальное количество конфет за ход
# max_n = 28  # максимальное количество конфет за ход

# # Объявление дополнительных переменных:
# ostatok = n
# take_user = 0
# flag_user = True

# def candies_game(message):
#     global ostatok, take_user, flag_user

#     # Бросок игральной кости
#     def Kosti():
#         res = randint(1, 6)
#         return res

#     # Вопрос пользователю (сколько брать)
#     def user_step_quesion():
#         answer = bot.send_message(message.chat.id, f'{message.from_user.first_name}, сколько возьмёшь?')
#         bot.register_next_step_handler(answer, user_step)

#     # Обработка ответа пользователя
#     def user_step(answer):
#         global take_user, flag_user
#         if answer.text.isdigit():
#             user_num = int(answer.text)
#             if user_num < min_n or user_num > max_n or user_num > ostatok:
#                 bot.send_message(message.chat.id, f'Ты ошибся! Взять нужно от {min_n} до {max_n} конфет и не больше остатка!')
#                 user_step_quesion()
#             else:
#                 take_user = user_num
#                 flag_user = False
#         else:
#             bot.send_message(message.chat.id, f'Ты ошибся! Нужно вводить число!')
#             user_step_quesion()

#     # Объявление правил игры
#     bot.send_message(message.chat.id, f'<b>Правила игры:</b>\nНа столе лежит {n} конфет. За один ход можно забрать не более чем {max_n} конфет.\nВсе конфеты оппонента достаются сделавшему последний ход!\nПервый ход определяется жеребьёвкой.', parse_mode='html')
#     time.sleep(3)

#     # Жеребьёвка
#     Player_1 = message.from_user.first_name
#     Player_2 = 'Bot'
#     bot.send_message(message.chat.id, '<b>Бросаем кости!</b>\nУ кого число будет больше, тот ходит первым!', parse_mode='html')
#     brosok_1 = 0
#     brosok_2 = 0
#     while brosok_1 == brosok_2:
#         brosok_1 = Kosti()
#         brosok_2 = Kosti()
#         time.sleep(2)
#         bot.send_message(message.chat.id, f'<b>{Player_1}</b>: {brosok_1}', parse_mode='html')
#         time.sleep(2)
#         bot.send_message(message.chat.id, f'<b>{Player_2}</b>: {brosok_2}', parse_mode='html')
#     if brosok_1 > brosok_2: 
#         first = Player_1
#         second = Player_2
#         bot.send_message(message.chat.id, f'Начинает игру <b>{Player_1}</b>!', parse_mode='html')
#     else:
#         first = Player_2
#         second = Player_1
#         bot.send_message(message.chat.id, f'Начинает игру <b>{Player_2}</b>!', parse_mode='html')
#     time.sleep(3)

#     # Берём по очереди конфеты со стола и определяем победителя
#     flag = True
#     while ostatok > 0 and flag == True:
#         bot.send_message(message.chat.id, f'<b>Сейчас на столе {ostatok} конфет!</b>', parse_mode='html')
#         if first == Player_2:
#             if ostatok <= max_n: 
#                 minus_1 = ostatok
#             else: 
#                 minus_1 = ostatok % (max_n + 1)
#                 if minus_1 == 0:
#                     minus_1 = randint(1, 28)
#             bot.send_message(message.chat.id, f'{first} взял {minus_1} конфет')
#             ostatok = ostatok - minus_1
#         else:
#             user_step_quesion()
#             while flag_user == True:
#                 time.sleep(1)
#             flag_user = True
#             ostatok = ostatok - take_user
#         if ostatok == 0:
#             bot.send_message(message.chat.id, f'<b>На столе осталось {ostatok} конфет! Игра окончена!\nПобедитель - {first}!</b>\n', parse_mode='html')
#             flag = False
#         else:
#             bot.send_message(message.chat.id, f'<b>Сейчас на столе {ostatok} конфет!</b>', parse_mode='html')
#             if second == Player_2:
#                 if ostatok <= max_n: 
#                     minus_2 = ostatok
#                 else: 
#                     minus_2 = ostatok % (max_n + 1)
#                     if minus_2 == 0:
#                         minus_2 = randint(1, 28)
#                 bot.send_message(message.chat.id, f'{second} взял {minus_2} конфет')
#                 ostatok = ostatok - minus_2
#             else:
#                 user_step_quesion()
#                 while flag_user == True:
#                     time.sleep(1)
#                 flag_user = True
#                 ostatok = ostatok - take_user
#             if ostatok == 0:
#                 bot.send_message(message.chat.id, f'<b>На столе осталось {ostatok} конфет! Игра окончена!\nПобедитель - {second}!</b>', parse_mode='html')
#                 flag = False
#     end_message(message)


# # Калькулятор для работы с рациональными и комплексными числами.
# # Объявление дополнительных переменных:
# number_1 = ''
# number_2 = ''
# act = ''
# flag_calc = True

# def calculator(message):
#     global number_1, number_2, act, flag_calc

#     # Запрос у пользователя первого числа
#     def first_user_quesion(message):
#         answer_1 = bot.send_message(message.chat.id, f'Введите первое число:')
#         bot.register_next_step_handler(answer_1, first_number)

#     # Запрос у пользователя второго числа
#     def second_user_quesion(message):
#         answer_1 = bot.send_message(message.chat.id, f'Введите второе число:')
#         bot.register_next_step_handler(answer_1, second_number)

#     # Обработка первого ответа пользователя
#     def first_number(answer):
#         global number_1, flag_calc
#         number_1 = answer.text
#         if ',' in number_1:
#             number_1 = number_1.replace(',', '.')
#         if number_1.count('.') == 1 and number_1.replace('.', '').isdigit()  or number_1.count('j') == 1:
#             flag_calc = False
#         else:
#             bot.send_message(message.chat.id, f'Вы ошиблись! Вводить можно число:\nцелое - 1, 2, 3 и т.д,\nдробное - 1.2, 3.1, 8.5 и т.д,\nкомплексное - 1 + 2j, 3 + 7j, 4 - 5j и т.д')
#             first_user_quesion(message)

#     # Обработка второго ответа пользователя
#     def second_number(answer):
#         global number_2, flag_calc
#         number_2 = answer.text
#         if ',' in number_2:
#             number_2 = number_2.replace(',', '.')
#         if number_2.count('.') == 1 and number_2.replace('.', '').isdigit()  or number_2.count('j') == 1:
#             flag_calc = False
#         else:
#             bot.send_message(message.chat.id, f'Вы ошиблись! Вводить можно число:\nцелое - 1, 2, 3 и т.д,\nдробное - 1.2, 3.1, 8.5 и т.д,\nкомплексное - 1 + 2j, 3 + 7j, 4 - 5j и т.д')
#             second_user_quesion(message)

#     # Определение числа (рациональное или комплексное)
#     def dif_number(number):
#         try:
#             return float(number)
#         except:
#             return complex(number.replace(' ', ''))

#     # Запрос действия у пользователя используя кнопки ввода
#     def operation(message):
#         markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
#         plus = types.KeyboardButton('+')
#         minus = types.KeyboardButton('-')
#         multiply = types.KeyboardButton('*')
#         divide = types.KeyboardButton('/')
#         markup.add(plus, minus, multiply, divide)
#         answer = bot.send_message(message.chat.id, '<b>Выберите действие:</b>', parse_mode='html', reply_markup=markup)
#         bot.register_next_step_handler(answer, actions)

#     # Обработка выбора действия
#     def actions(answer):
#         global act, flag_calc
#         act = answer.text
#         flag_calc = False

#     # Вычисление ответа
#     def calculation(a, b, oper):
#         if oper == '+':
#             return a + b
#         elif oper == '-':
#             return a - b
#         elif oper == '*':
#             return a * b
#         elif oper == '/':
#             return a / b

#     # Ожидание, чтобы код не шел дальше, пока flag_calc == True
#     def waiting():
#         global flag_calc
#         while flag_calc == True:
#             time.sleep(1)
#         flag_calc = True

#     # Выполнение алгоритма калькулятора + логирование
#     first_user_quesion(message)
#     waiting()
#     second_user_quesion(message)
#     waiting()
#     operation(message)
#     waiting()
#     res = calculation(dif_number(number_1), dif_number(number_2), act)
#     bot.send_message(message.chat.id, f'<b>Ответ: {res}</b>', parse_mode='html')
#     with open('Log.txt', 'a') as f:
#         f.write(f'{time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())}:  {number_1} {act} {number_2} = {res}\n')
#     end_message(message)

# bot.polling(none_stop=True)

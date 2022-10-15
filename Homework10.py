# Задача. 
# 21 очко с командой, при вызове которой, бот говорит, кто сколько раз выиграл(выводит счет)

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import choice as ch
import time


bot = Bot(token='5614343760:AAHoM5PFkDNPA-Urzi7STHjG9904YSl8ySc')
updater = Updater(token='5614343760:AAHoM5PFkDNPA-Urzi7STHjG9904YSl8ySc')
dispatcher = updater.dispatcher

data = {6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 'Валет': 4, 'Дама': 4, 'Король': 4,
        'Туз': 4}

count_points_user = []
count_points_bot = 0
win_count_user = 0
win_count_bot = 0
not_win_count = 0

WINNER = None # 0 - ничья, 1 - выиграл пользователь, -1 - выиграл бот
BOT = 1
USER = 2


def help(update, context):
    context.bot.send_message(update.effective_chat.id, f'Список команд:\n1. Старт игры - /start\n2. Взять ещё - /yet\n3. Больше не брать - /stop\n4. Показать счёт - /res\n5. Обнулить счёт - /zero\n6. Показать список команд - /help')


def res(update, context):
    context.bot.send_message(update.effective_chat.id, f'Количество побед за всё время:\nБот - {win_count_bot}\nПользователь - {win_count_user}\nНичья - {not_win_count}\n\nОбнулить счёт - /zero')


def zero(update, context):
    global win_count_bot, win_count_user, not_win_count
    win_count_user = 0
    win_count_bot = 0
    not_win_count = 0
    context.bot.send_message(update.effective_chat.id, 'Обнуление счёта выполнено успешно!')


def check(n):
    if type(n) == int:
        return n
    elif 'в' in n.lower():
        return 2
    elif 'д' in n.lower():
        return 3
    elif 'к' in n.lower():
        return 4
    elif 'т' in n.lower():
        return 11


def winner_check(user, bots):
    global WINNER
    if sum(user) > 21 and bots < 22 or sum(user) < bots and sum(user) < 21 and bots <= 21:
        WINNER = -1
    elif bots > 21 and sum(user) < 22 or sum(user) > bots and sum(user) <= 21 and bots < 21:
        WINNER = 1
    elif sum(user) > 21 and bots > 21 or sum(user) == bots:
        WINNER = 0


def start(update, context):
    global count_points_user, count_points_bot, win_count_user, win_count_bot, not_win_count, WINNER

    count_points_user.clear()
    count_points_bot = 0
    WINNER = None

    for i in range(2):
        data_object = ch(list(data.keys()))
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_user.append(points)

    for i in range(2):
        data_object = ch(list(data.keys()))
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_bot += points

    a = '\n'.join([str(i) for i in count_points_user])
    context.bot.send_message(update.effective_chat.id, f"{a}\nСумма: {sum(count_points_user)}")
    if sum(count_points_user) > 21 or count_points_bot > 21:
        context.bot.send_message(update.effective_chat.id, f"Сумма у Бота: {count_points_bot}")
        if sum(count_points_user) > 21 and count_points_bot < 22:
            win_count_bot += 1
            context.bot.send_message(update.effective_chat.id, "У тебя перебор! Выиграл Бот!")
        elif count_points_bot > 21 and sum(count_points_user) < 22:
            win_count_user += 1
            context.bot.send_message(update.effective_chat.id, "У Бота перебор! Ты выиграл!")
        elif sum(count_points_user) > 21 and count_points_bot > 21:
            not_win_count += 1
            context.bot.send_message(update.effective_chat.id, "Перебор у обоих! Вы лузеры!")
        context.bot.send_message(update.effective_chat.id, "Игра окончена!\nНачать заново - /start\nПоказать счёт - /res\nПомощь - /help")
    else:
        context.bot.send_message(update.effective_chat.id, f'{update.effective_user.first_name}, что делаем дальше?\nВзять ещё - /yet\nОстановиться - /stop')


def yet(update, context):
    global count_points_user, win_count_bot
    if sum(count_points_user) <= 21 and WINNER == None:
        data_object = ch(list(data.keys()))
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_user.append(points)

        a = '\n'.join([str(i) for i in count_points_user])
        context.bot.send_message(update.effective_chat.id, f"{a}\nСумма: {sum(count_points_user)}")
        if sum(count_points_user) > 21:
            win_count_bot += 1
            context.bot.send_message(update.effective_chat.id, f"Перебор! {update.effective_user.first_name}, ты проиграл")
            context.bot.send_message(update.effective_chat.id, "Игра окончена!\nНачать заново - /start\nПоказать счёт - /res\nПомощь - /help")
        else:
            context.bot.send_message(update.effective_chat.id, f'{update.effective_user.first_name}, что делаем дальше?\nВзять ещё - /yet\nОстановиться - /stop')
    else:
        context.bot.send_message(update.effective_chat.id, "Игра окончена!\nНачать заново - /start\nПоказать счёт - /res\nПомощь - /help")


def stop(update, context):
    if WINNER == None and sum(count_points_user) <= 21:
        global count_points_bot, win_count_user, win_count_bot, not_win_count
        context.bot.send_message(update.effective_chat.id, 'Вы закончили набор, теперь набирает Бот')
        time.sleep(3)
        while count_points_bot < 18:
            data_object = ch(list(data.keys()))
            while data[data_object] == 0:
                data_object = ch(list(data.keys()))
            data[data_object] -= 1
            points = check(data_object)
            count_points_bot += points

        winner_check(count_points_user, count_points_bot)
        context.bot.send_message(update.effective_chat.id, f'Кол-во очков у Бота: {count_points_bot}\n'
                                                           f'Кол-во очков у {update.effective_user.first_name}: {sum(count_points_user)}')
        if WINNER == -1:
            win_count_bot += 1
            context.bot.send_message(update.effective_chat.id, 'Выиграл Бот!')
        elif WINNER == 1:
            win_count_user += 1
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, ты выиграл!")
        elif WINNER == 0:
            not_win_count += 1
            context.bot.send_message(update.effective_chat.id, 'Вы с Ботом лузеры!')
    context.bot.send_message(update.effective_chat.id, "Игра окончена!\nНачать заново - /start\nПоказать счёт - /res\nПомощь - /help")


start_handler = CommandHandler('start', start)
still_handler = CommandHandler('yet', yet)
stop_handler = CommandHandler('stop', stop)
result_handler = CommandHandler('res', res)
zero_handler = CommandHandler('zero', zero)
help_handler = CommandHandler('help', help)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(still_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(result_handler)
dispatcher.add_handler(zero_handler)
dispatcher.add_handler(help_handler)

updater.start_polling()
updater.idle()  # ctrl + c

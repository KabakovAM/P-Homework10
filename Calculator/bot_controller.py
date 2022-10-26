import telebot
import token_id
import exception
import model_sum
import model_sub
import model_mult
import model_div
import logg

bot = telebot.TeleBot(token_id.token_id())


@bot.message_handler(content_types=['text'])
def start_calc(message):
    logg.opertion_logger(message.from_user.id,
                         message.from_user.first_name, 'start_calc', message.text)
    if message.text == '/start':
        msg = bot.send_message(message.from_user.id,
                               ('Добро пожаловать в калькулятор!\nВыберите опцию:\n\
1 - Рациональное число\n2 - Комплексное число\n3 - Выйти из программы'))
        return bot.register_next_step_handler(msg, main_menu)
    else:
        msg = bot.send_message(
            message.from_user.id, ('Введите "/start", чтобы включить калькулятор.'))
        return bot.register_next_step_handler(msg, start_calc)


def main_menu(message):
    logg.opertion_logger(message.from_user.id,
                         message.from_user.first_name, 'main_menu', message.text)
    global typ
    if not exception.type_op(message.text, 3):
        msg = bot.send_message(message.from_user.id,
                               ('Ошибка ввода! Повторите ввод!'))
        return bot.register_next_step_handler(msg, main_menu)
    typ = exception.type_op(message.text, 3)
    if typ == 1:
        msg = bot.send_message(message.from_user.id,
                               ('Выберете опцию:\n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n\
5 - Возведение в степень\n6 - Извлечение квадратного корня\n7 - Выйти в предыдущее меню'))
        return bot.register_next_step_handler(msg, sub_menu_1)
    if typ == 2:
        msg = bot.send_message(message.from_user.id,
                               ('Выберете опцию:\n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n\
5 - Возведение в степень\n6 - Выйти в предыдущее меню'))
        return bot.register_next_step_handler(msg, sub_menu_2)
    if typ == 3:
        msg = bot.send_message(
            message.from_user.id, ('Введите "/start", чтобы включить калькулятор.'))
        return bot.register_next_step_handler(msg, start_calc)


def sub_menu_1(message):
    logg.opertion_logger(message.from_user.id,
                         message.from_user.first_name, 'sub_menu_1', message.text)
    global op
    if not exception.type_op(message.text, 7):
        msg = bot.send_message(message.from_user.id,
                               ('Ошибка ввода! Повторите ввод!'))
        return bot.register_next_step_handler(msg, sub_menu_1)
    op = exception.type_op(message.text, 7)
    if 0 < op < 5:
        msg = bot.send_message(message.from_user.id, ('Введите первое число:'))
        return bot.register_next_step_handler(msg, get_number)
    if op == 5:
        msg = bot.send_message(message.from_user.id,
                               ('Введите основание степени:'))
        return bot.register_next_step_handler(msg, get_number)
    if op == 6:
        msg = bot.send_message(message.from_user.id,
                               ('Введите подкоренное выражение:'))
        return bot.register_next_step_handler(msg, calculation)
    if op == 7:
        msg = bot.send_message(message.from_user.id,
                               ('Добро пожаловать в калькулятор!\nВыберите опцию:\n\
1 - Рациональное число\n2 - Комплексное число\n3 - Выйти из программы'))
        return bot.register_next_step_handler(msg, main_menu)


def sub_menu_2(message):
    logg.opertion_logger(message.from_user.id,
                         message.from_user.first_name, 'sub_menu_2', message.text)
    global op
    if not exception.type_op(message.text, 6):
        msg = bot.send_message(message.from_user.id,
                               ('Ошибка ввода! Повторите ввод!'))
        return bot.register_next_step_handler(msg, sub_menu_2)
    op = exception.type_op(message.text, 6)
    if 0 < op < 5:
        msg = bot.send_message(message.from_user.id,
                               ('Первое число.\nВведите вещественную часть:'))
        return bot.register_next_step_handler(msg, get_complex, 0)
    if op == 5:
        msg = bot.send_message(message.from_user.id,
                               ('Основание степени.\nВведите вещественную часть:'))
        return bot.register_next_step_handler(msg, get_complex, 0)
    if op == 6:
        msg = bot.send_message(message.from_user.id,
                               ('Добро пожаловать в калькулятор!\nВыберите опцию:\n\
1 - Рациональное число\n2 - Комплексное число\n3 - Выйти из программы'))
        return bot.register_next_step_handler(msg, main_menu)


def get_number(message):
    logg.opertion_logger(message.from_user.id,
                         message.from_user.first_name, 'get_number', message.text)
    global num_1
    if not exception.number(message.text):
        msg = bot.send_message(message.from_user.id,
                               ('Ошибка ввода! Повторите ввод!'))
        return bot.register_next_step_handler(msg, get_number)
    num_1 = exception.number(message.text)
    if 0 < op < 5:
        msg = bot.send_message(message.from_user.id, ('Введите второе число:'))
        return bot.register_next_step_handler(msg, calculation)
    if op == 5:
        msg = bot.send_message(message.from_user.id,
                               ('Введите показатель степени:'))
        return bot.register_next_step_handler(msg, calculation)


def get_complex(message, compl_1):
    logg.opertion_logger(message.from_user.id,
                         message.from_user.first_name, 'get_complex', message.text)
    global num_1
    global num_2
    global num_3
    if not exception.number(message.text):
        msg = bot.send_message(message.from_user.id,
                               ('Ошибка ввода! Повторите ввод!'))
        return bot.register_next_step_handler(msg, get_complex, compl_1)
    if compl_1 == 0:
        num_1 = exception.number(message.text)
        compl_1 += 1
        if 0 < op < 5:
            msg = bot.send_message(message.from_user.id,
                                   ('Первое число.\nВведите мнимую часть:'))
            return bot.register_next_step_handler(msg, get_complex, compl_1)
        if op == 5:
            msg = bot.send_message(message.from_user.id,
                                   ('Основание степени.\nВведите мнимую часть:'))
            return bot.register_next_step_handler(msg, get_complex, compl_1)
    if compl_1 == 1:
        num_2 = exception.number(message.text)
        compl_1 += 1
        if 0 < op < 5:
            msg = bot.send_message(
                message.from_user.id, ('Второе число.\nВведите вещественную часть:'))
            return bot.register_next_step_handler(msg, get_complex, compl_1)
        if op == 5:
            msg = bot.send_message(message.from_user.id,
                                   ('Показатель степени.\nВведите вещественную часть:'))
            return bot.register_next_step_handler(msg, get_complex, compl_1)
    if compl_1 == 2:
        num_3 = exception.number(message.text)
        compl_1 += 1
        if 0 < op < 5:
            msg = bot.send_message(message.from_user.id,
                                   ('Второе число.\nВведите мнимую часть:'))
            return bot.register_next_step_handler(msg, calculation)
        if op == 5:
            msg = bot.send_message(message.from_user.id,
                                   ('Показатель степени.\nВведите мнимую часть:'))
            return bot.register_next_step_handler(msg, calculation)


def calculation(message):
    logg.opertion_logger(message.from_user.id,
                         message.from_user.first_name, 'calculation', message.text)
    global num_1
    global num_2
    global num_3
    dic = {1: '+', 2: '-', 3: '*', 4: '/', 5: '^', 6: '\u221a'}
    if not exception.number(message.text):
        msg = bot.send_message(message.from_user.id,
                               ('Ошибка ввода! Повторите ввод!'))
        return bot.register_next_step_handler(msg, calculation)
    if typ == 1:
        num_2 = exception.number(message.text)
    if typ == 2:
        num_4 = exception.number(message.text)
        num_1 = complex(num_1, num_2)
        num_2 = complex(num_3, num_4)
    if op == 1:
        result = model_sum.init(num_1, num_2)
    if op == 2:
        result = model_sub.init(num_1, num_2)
    if op == 3 or op == 5:
        result = model_mult.init(num_1, num_2, op, typ)
    if op == 4:
        result = model_div.init(num_1, num_2, op, typ)
    if op == 6:
        num_1, num_2 = num_2, 1
        result = model_div.init(num_1, num_2, op, typ)
        msg = bot.send_message(message.from_user.id, (
            f'\n{dic[op]}{num_1} = {result}\nВведите "/start", чтобы продолжить работу с калькулятором.'))
        return bot.register_next_step_handler(msg, start_calc)
    else:
        msg = bot.send_message(message.from_user.id, (
            f'\n{num_1} {dic[op]} {num_2} = {result}\nВведите "/start", чтобы продолжить работу с калькулятором.'))
        return bot.register_next_step_handler(msg, start_calc)


bot.polling(none_stop=True, interval=0)

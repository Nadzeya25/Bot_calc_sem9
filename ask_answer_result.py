# **запуск бота в файлк error_mes_go**

from logg import logging
import telebot  
from telebot import types
op = 0
sign_op = 0

my_bot = telebot.TeleBot('5924802034:AAEB7qD9p8lc6a5HDWiVstiQaHJwwGx4CZM')

@my_bot.message_handler(commands = ["start"])
def start(message):
    my_bot.send_message(message.chat.id, f"бот-калькулятор целых чисел готов к работе, нажмите 👉 /button для выбора действия") 

@my_bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    but1 = types.KeyboardButton("посчитать сумму")    
    but2 = types.KeyboardButton("посчитать разность")
    but3 = types.KeyboardButton("посчитать произведение")
    but4 = types.KeyboardButton("посчитать обычное деление")
    but5 = types.KeyboardButton("посчитать целочисленное деление")
    but6 = types.KeyboardButton("посчитать остаток от деления")
    but7 = types.KeyboardButton("посчитать степень числа")
    but_exit = types.KeyboardButton("закончить работу с калькулятором")
    
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)
    markup.add(but6)
    markup.add(but7)
    markup.add(but_exit)
       
    my_bot.send_message(message.chat.id, "выбери вариант ниже 👇", reply_markup=markup )

from math_op import* # импортирует всё из модуля
from error_mes_go import*

def right_do_it(message):
    my_bot.send_message(message.chat.id, "напиши два целых числа через пробел")
    my_bot.register_next_step_handler(message, result_op)

@my_bot.message_handler(content_types = ['text'])
def controller(message):
    global op
    global sign_op
    
    match message.text:
        case "посчитать сумму":
            op = sum
            sign_op = "+"
            right_do_it(message)

        case "посчитать разность":
            op = sub
            sign_op = "-"
            right_do_it(message)

        case "посчитать произведение":
            op = mult
            sign_op = "*"
            right_do_it(message)

        case "посчитать обычное деление":
            op = div_all
            sign_op = "/"
            right_do_it(message)

        case "посчитать целочисленное деление":
            op = div_int
            sign_op = "//"
            right_do_it(message)

        case "посчитать остаток от деления":
            op = div_rem
            sign_op = "%"
            right_do_it(message)

        case "посчитать степень числа":
            op = pow
            sign_op = "^"
            right_do_it(message)
        case "закончить работу с калькулятором":
            my_bot.send_message(message.chat.id, "всё, закончили, идите пить чай ☕")
    
        case _:
            my_bot.send_message(message.chat.id, "сначала нужно выбрать кнопку с действием  🔤")
            error_button(message)  #возвращаемся к меню
            logging.error("Error")

           
def result_op(message):    
    global op
    global sign_op
    try:
        text1 = message.text
        i = text1.index(' ')
        num1 = text1[:i]
        num2 = text1[i+1:]
        res = op(num1, num2)
        my_bot.send_message(message.chat.id, f"{num1} {sign_op} {num2} = {res}")
        button(message)  #возвращаемся к меню
    except:
        error_nums(message)    
        logging.error("Error")


my_bot.infinity_polling()






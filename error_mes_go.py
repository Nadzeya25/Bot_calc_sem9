
# запуск бота отсюда
from logg import logging
from ask_answer_result import my_bot
from ask_answer_result import button

def error_button(message):  # вместо нажатия кнопки пишет что-то руками, вводит числа
    my_bot.send_message(message.chat.id, "🙅 ничего не пиши, просто кликни действие кнопкой снизу 👇")
    button(message)
    logging.error("ошибка выбора действия")

def error_nums(message):    # неправильно вводит числа или вместо этого жмет кнопки
    my_bot.send_message(message.chat.id, "😖 ошибка ввода: возможно , вы пытаетесь разделить на ноль ")
    button(message)
    logging.error("ошибка ввода")


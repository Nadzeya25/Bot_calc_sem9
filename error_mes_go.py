
# запуск бота отсюда
from logg import logging
from main import my_bot
from main import button

def error_button(message):  # вместо нажатия кнопки пишет что-то руками, вводит числа
    my_bot.send_message(message.chat.id, "🙅 ничего не пиши, просто кликни действие кнопкой снизу 👇")
    button(message)
    logging.error("Error")

def error_nums(message):    # неправильно вводит числа или вместо этого жмет кнопки
    my_bot.send_message(message.chat.id, "😖 Вы не так вводите! Давайте заново - сначала кнопка действия, потом ** число пробел число ** ")
    button(message)
    logging.error("Error")
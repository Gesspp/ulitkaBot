import telebot
from telebot import types

bot = telebot.TeleBot('8064482140:AAFGqr48VTiLHjYAanI1wWbJ4sMA7JHhmdU')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton('Want to make a post?', callback_data='make_post')
    btn3 = types.InlineKeyboardButton('Information', callback_data='info')
    markup.add(btn2, btn3)

    bot.send_message(message.chat.id, 'This bot is created for making posts', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'info':
        bot.send_message(call.message.chat.id, "This bot is for making posts")
    elif call.data == 'make_post':
        msg = bot.send_message(call.message.chat.id, "Please enter your post text")
        bot.register_next_step_handler(msg, process_post)


def process_post(message):
    mess = message.text
    bot.send_message(-1002441261910, "Post: " + mess + f" @{message.from_user.username}")
    bot.send_message(-1002461746865, "Post: " + mess)


bot.polling()
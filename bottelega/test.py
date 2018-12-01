import telebot
from telebot import types

bot = telebot.TeleBot('666313419:AAG3ZIwXgb-xLoTryb2oVMmE950r52cKLZw')


@bot.message_handler(commands =["start"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="1", callback_data="1")
    but_2 = types.InlineKeyboardButton(text="2", callback_data="2")
    key.add(but_1, but_2)
    bot.send_message(message.chat.id, "текст" , reply_markup = key)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == "1":
        bot.send_message(c.messagec.caht.id, "text")
    elif c.data == "2":
        bot.send_message(c.messagec.caht.id, "text2")



if __name__ == '__main__':
    bot.polling(none_stop=True)
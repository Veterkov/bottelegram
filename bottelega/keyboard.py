import constant
import telebot
from telebot import types
bot = telebot.TeleBot(constant.TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
   main_greeting = 'Main greeting text'
   main_menu = telebot.types.ReplyKeyboardMarkup(True, False)
   main_menu.row('Answer 1')
   main_menu.row('Answer 2', 'Answer 3')
   bot.send_message(message.from_user.id, main_greeting, reply_markup=main_menu)


@bot.message_handler()
def handle_text(message):
    if message.text == 'Answer 1':
        answer_1_text = 'Answer 1 text'
        answer_1_menu = telebot.types.ReplyKeyboardMarkup(True, False)
        answer_1_menu.row('Option 1')
        answer_1_menu.row('Option 2')
        answer_1_menu.row('Back') #"Back" should bring user to the main_menu
        bot.send_message(message.from_user.id, answer_1_text, reply_markup=main_flavor_menu)

    elif message.text == 'Option 1':
            option_1_text = 'Select from one of the categories for further help'
            option_1_menu = telebot.types.ReplyKeyboardMarkup(True, False)
            option_1_menu.row('Category 1', 'Category 2')
            option_1_menu.row('Category 3')
            option_1_menu.row('Back', 'To Main') #"Back" should bring user to
                                             #the answer_1_menu and "To Main"
                                             #should bring one to main_menu

            bot.send_message(message.from_user.id, option_1_text, reply_markup=option_1_menu)

    elif message.text == 'Back':
            bot.send_message(message.from_user.id, '.', reply_markup=answer_1_menu-1)

    elif message.text == 'Back':
            bot.send_message(message.from_user.id, '.', reply_markup=option_1_menu-1)

    elif message.text == 'To Main':
            bot.send_message(message.from_user.id, option_1_text, reply_markup=main_menu)




bot.polling(none_stop=True, interval=0)
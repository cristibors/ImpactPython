import telebot
from telebot import types
from telebot.util import content_type_media

TOKEN = "7894765971:AAE5mEZ3cSnkOlGohSzm6AQDqF5LDNrexbM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    catalog = types.KeyboardButton('Catalog🗃️')
    basket = types.KeyboardButton('Cos🗑️')
    orders = types.KeyboardButton('Comenzi🚛')
    feedback = types.KeyboardButton('FeedBack💭')

    markup.add(catalog, basket, orders, feedback)

    send_message = "<b>Salut 👋</b>\nBine ați venit la magazinul nostru online!"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text=="Catalog🗃️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tshirts = types.KeyboardButton('Tricouri 👕')
        jeans = types.KeyboardButton('Blugi 👖')
        shoes = types.KeyboardButton('Incaltaminte 👟')
        shirts = types.KeyboardButton('Camasi 👔')
        suit = types.KeyboardButton('Costume 🕴️')
        dress = types.KeyboardButton('Rochii 👗')
        back = types.KeyboardButton('Inapoi 🔙')
        markup.add(tshirts,jeans,shoes,shirts,suit,dress,back)
        send_message ="Minunat!Ce anume va intereseaza?"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    elif message.text == "Incaltaminte 👟":
        markup=types.InlineKeyboardMarkup()
        unity=types.InlineKeyboardButton("Accesati",url="https://intertop.kz/brands/")
        markup.add(unity)
        send_message="Inteaga colectie poate fi vizualizeata pe site-ul nostru👀"
        bot.send_message(message.chat.id, send_message,parse_mode='html',reply_markup=markup)

    elif message.text=="Inapoi 🔙":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        catalog = types.KeyboardButton('Catalog🗃️')
        basket = types.KeyboardButton('Cos🗑️')
        orders = types.KeyboardButton('Comenzi🚛')
        feedback = types.KeyboardButton('FeedBack💭')

        markup.add(catalog, basket, orders, feedback)

        send_message = "<b>Salut 👋</b>\nBine ați venit la magazinul nostru online!"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"bot polling failed {e}")

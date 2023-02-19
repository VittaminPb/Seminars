import telebot
from telebot import types

bot = telebot.TeleBot("6052126529:AAHdKiwm223o0OCswmBL1tVz-_otABUewwE")

@bot.message_handler(commands = ["start"])

def start(message):
    bot.send_message(message.chat.id, "Hello ))")

@bot.message_handler(commands = ["fio"])

def fio(message):
    bot.send_message(message.chat.id, "Напиши свои фамилию и имя в одной строке")
    bot.register_next_step_handler(message, sentance)

def sentance(message):
    text = message.text
    surname = text.split()[0]
    name = text.split()[1]
    bot.send_message(message.chat.id, f"Тебя зовут - {name}, фамилия - {surname}")

@bot.message_handler(commands = ["but"])
def but(message):
    bot.send_message(message.chat.id, "/button")

@bot.message_handler(commands = ["button"])
def button(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("Сделать предложение")
        but2 = types.KeyboardButton("Узнать время")
        markup.add(but1)
        markup.add(but2)
        bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)



print("Bot start")
bot.infinity_polling()
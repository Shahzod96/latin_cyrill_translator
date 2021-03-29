"""
Created on Sat Mar 27 2021

@author: acer
"""

import telebot
from transliterate import to_latin, to_cyrillic

TOKEN = "1665937395:AAHlSSmD7e-6__vIOkJQkXH-9LbyDDFpBto"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    javob = "Assalomu alaykum tarjimon botimizga hush kelibsiz"
    javob += "\nTarjima qilmoqchi bo'lgan matningizni kiriting:"
    javob += "\nАссалому алайкум таржимон ботимизга ҳуш келибсиз!"
    javob += "\nТаржима қилмоқчи бўлган матнингизни киритинг:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))

bot.polling()

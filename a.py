import telebot
import json 

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.from_user.id, 'Привет-пока')

bot.polling(none_stop=True, interval=0, timeout=120)
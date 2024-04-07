import telebot
import json 

def get_token():
    token = ''
    with open('token.jsons') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

TOKEN = get_token() + '1'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.from_user.id, 'Привет-пока')

bot.polling(none_stop=True, interval=0, timeout=120)
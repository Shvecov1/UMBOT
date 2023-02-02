import telebot
import emoji
from dotenv import load_dotenv
import os
load_dotenv()
os.getenv("TELEGRAM_BOT_KEY")
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_KEY"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Введите число")

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == message.text:
        message_type = int(message.text)
        if message_type < 256:
            mess_bin = bin(message_type)[2:][::-1]


            mess_bot = '12345678'
            mess_bot = mess_bot.replace('1', '1️⃣')
            mess_bot = mess_bot.replace('2', '2️⃣')
            mess_bot = mess_bot.replace('3', '3️⃣')
            mess_bot = mess_bot.replace('4', '4️⃣')
            mess_bot = mess_bot.replace('5', '5️⃣')
            mess_bot = mess_bot.replace('6', '6️⃣')
            mess_bot = mess_bot.replace('7', '7️⃣')
            mess_bot = mess_bot.replace('8', '8️⃣\n')
            mess_bin = mess_bin.replace('1', '🟩')
            mess_bin = mess_bin.replace('0', '⬛')

            bot.send_message(message.chat.id, mess_bot + mess_bin.ljust(8, '⬛'), parse_mode='html')
        else:
            bot.send_message(message.chat.id, 'Введите число от 1 до 255', parse_mode='html')




bot.infinity_polling()
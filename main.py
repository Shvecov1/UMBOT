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
        mess_bin = bin(message_type)[2:]
        mess_bin1 = str(mess_bin)
        mess_bin2 = str(mess_bin)
        zero = '\x30\xE2\x83\xA3'
        mess_bin1 = mess_bin1.replace('1', '⬜')
        mess_bin1 = mess_bin1.replace('0', '🟥')
        mess_bin2 = mess_bin2.replace('1', '⚪')
        mess_bin2 = mess_bin2.replace('0', '🔴')

        bot.send_message(message.chat.id, mess_bin1.ljust(8, '🟥'), parse_mode='html')
        bot.send_message(message.chat.id, mess_bin2.ljust(8, '🔴'), parse_mode='html')




bot.infinity_polling()
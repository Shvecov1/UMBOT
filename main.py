import telebot

bot = telebot.TeleBot("5852221523:AAElyDPHkXaJf8Lb8ZIxQvIheOwTAlUpD-s")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Введите число")

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == message.text:
        message_type = int(message.text)
        mess = bin(message_type)[2:]
        print(mess)
        bot.send_message(message.chat.id, mess.ljust(8,'0'), parse_mode='html')




bot.infinity_polling()
#
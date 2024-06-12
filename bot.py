import telebot

with open('/KVARCEVIEhelp/bot_token.txt', 'r') as file:
    bot_token = file.read().strip()

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет. Я — твой будущий инлайн бот, а так же помощник. На данный момент я нахожусь в разработке, поэтому, пожалуйста, ожидай моего появления!")

bot.polling()

import telebot
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
token_file_path = os.path.join(script_dir, '../bot_token.txt')

with open(token_file_path, 'r') as file:
    bot_token = file.readline().strip()

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет. Я — твой будущий инлайн бот, а также помощник. На данный момент я нахожусь в разработке, поэтому, пожалуйста, ожидай моего появления!")

if __name__ == "__main__":
    try:
        bot.polling()
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")

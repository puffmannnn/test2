import telebot
import os

# Получаем токен бота из переменных окружения
TOKEN = os.getenv('7735911622:AAFOI1P7dR4uRKIL1A_04SBR0kp7hND89us')
bot = telebot.TeleBot(TOKEN)

# Ответ на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот на Render!")

# Ответ на любые текстовые сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.polling(none_stop=True)

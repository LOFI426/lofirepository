import telebot
import requests
import json

bot = telebot.TeleBot('8391347523:AAFkJJ8gGThjRlzo6mvqHYE0gZLCNbmgm3U')

api_key = 'cc2ba876736132e270670f8d7ebb0aef' # токен (1-е сообщение)

base_url = 

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    welcome_text = (
        'Привет! Я погода бот.\n\n'
        'Используйте команду /weather для получения прогноза .\n\n'
        'Пример:\n'
        '/weather Moskow\n'
        '/weather London\n'
        '/weather Tokyo\n\n'
        'Введите название города на английском языке.'
    )
    bot.reply_to(message, welcome_text)
    
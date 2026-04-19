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

@bot.message_handler(commands = ['weather'])
def get_weather(message):
    city = message.text.replace('/weather','').strip()

    if not city:
        bot.reply_to(
            message,
            'Пожалуйста, укажите название города\n'
            'Пример: /weather Moscow'

        )
        return
    try:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric',
            'lang': 'ru'
        }

        responce = requests.get(base_url, params = params)
        data = response.json()

        if respons.status_code != 200:
            if data.get('cod') == '404':
                bot.reply_to(message, f'Город "{city}" не найден. Проверьте написание')
            else:
                bot.reply_to(message, 'Ошибка при получении данных о погоде.')
                return
    
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        presure = data['main']['pressure']
        wind_speed = data['wind']['speed']
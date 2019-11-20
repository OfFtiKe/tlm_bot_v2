import telebot

TOKEN = '1016008776:AAFZfsBERa9MGDQu-qtg1SWV7ocMamAIfe4'
bot = telebot.TeleBot(TOKEN )

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling(none_stop=True, interval=0, timeout=20)

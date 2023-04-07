import telebot
import db

# Установка бота
bot = telebot.TeleBot("token")

# Приветственное сообщение от бота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text.lower() == 'привет':
            bot.send_message(message.from_user.id, 'Привет! Ваши данные добавлены в базу данных!')
            pass

        db.db_table_val()

bot.polling(non_stop=True)



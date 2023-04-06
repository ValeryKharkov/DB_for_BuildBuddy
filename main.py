import telebot

# Установка бота
bot = telebot.TeleBot("6034420797:AAHEjTuev9sWhr2PgKWpbIsH0SY_bV1I07Q")

# Приветственное сообщение от бота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Test_DB_for_BuildBuddy')


bot.infinity_polling()

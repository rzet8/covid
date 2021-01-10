import telebot

from parse import covid

token = "1504111420:AAH3V0n_MGkGMWkws_8xTmD1UZ6_igrac-Q"

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard.row("Получить посл. новости")

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.send_message(message.chat.id, f"😎 Привет <b>{message.chat.first_name}</b>!\n😷 Я отправляю данные о <i>коронавирусе</i> в городе <b>Иркутск</b>!", parse_mode="HTML", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_data(message):
    if message.text == "Получить посл. новости":
        data = covid()
        bot.send_photo(message.chat.id, data[0], data[1])
    
    else:
        bot.reply_to(message, "🙃 Я не знаю такую комманду!")


if __name__ == "__main__":
    bot.polling(True)
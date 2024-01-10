#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6735472029:AAHH432dTsZaabjG_44Lr7xqb4YbqznR6Bk'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Написать мне в личку")
	item3 = types.KeyboardButton("Аненкдот дня")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Халоха тебе от Билли Херрингтона, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/Kisel-inc')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/Vivalium')
		elif message.text == 'Аненкдот дня':
			bot.send_message(message.chat.id, 'https://www.anekdot.ru/release/anekdot/day/')
		else:
			bot.send_message(message.chat.id, 'Ты чё то перепутал😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods

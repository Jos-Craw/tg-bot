import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

goodword = ['Ты лучше всех❤', 'Замечательно выглядишь❤', '❤Обожаю тебя ❤', '❤Обожаю смотреть в твои глаза❤',
            'Люблю тебя❤']
kino = ['Прогулка по городу🏙', "Поход в бар🍺", "Поход в кино🎦", "Поход в кафе🍣", "Отдых дома🏘"]
mese = ''

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("Другое")
    item3 = types.KeyboardButton("❤ Комплимент")
    item4 = types.KeyboardButton('💖 Случайное свидание')
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы радовать всех ".
                     format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '❤ Комплимент':
            bot.send_message(message.chat.id, str(random.choice(goodword)))
        elif message.text == '💖 Случайное свидание':
            bot.send_message(message.chat.id, str(random.choice(kino)))
        elif message.text == "Другое":
            bot.send_message(message.from_user.id, 'Напиши, что ты хочешь поделать c Пашей')
            bot.register_next_step_handler(message, get_name)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


def get_name(message):
    global mese
    mese = message.text
    bot.send_message(673847179,'Геля хочет: '+mese)


bot.polling(none_stop=True)

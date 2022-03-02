from ast import Global
import telebot

from telebot import types

import requests

s_city = "Moscow,RU"
appid = "261e523ee42b698e0f420388a7a862d9"


token = "5184527373:AAHf8xr7QFk3nCLWLr_3JDoAk0oGIQ4haeA"
bot = telebot.TeleBot(token)
AList = []
k2 = ''



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("список", "cколько у меня тайтлов", "чё глянуть", "погода", "погода на неделю", "/help", "/del", "/anime")
    bot.send_message(message.chat.id, 'Привет! Я твой аниме бот) Если хочешь узнать что я умею, жмякай на кнопку /help', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу вести твой список аниме \n чтобы посмотреть свой список пиши - список \n Чтобы добавить аниме в список пиши - добавить название аниме \n а если ты криворукий, то и для тебя найдётся команда пиши - удалить название анимехи \n Также могу посоветовать аниме для этого пиши - чё глянуть \n Ещё я могу подсказать, сколько у тебя тайтлов  в списке, для этого пиши - сколько у меня тайтлов \n /del - обнулить список \n /anime - ссылка на сайт где можно посмотреть аниме')

@bot.message_handler(commands=['del'])
def start_message(message):
    global k2
    AList.clear()
    k2 = ''
    bot.send_message(message.chat.id, 'Список обнулён!')
@bot.message_handler(commands=['anime'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://animego.org/')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "чё глянуть":
        bot.send_message(message.chat.id, 'посмотри вот это, не пожалеешь ;) \n boku no piko')
    if "добавить" == message.text.lower().split(' ')[0]: 

        AList.append(message.text[9:])
        global k2
        k1 = len(AList)
        k3 = k1 - 1
        k = AList[k3]
        
        k2 = k2 + k + '\n'

        
        bot.send_message(message.chat.id, 'Готово, твоё аниме в списке :)')
        bot.send_message(message.chat.id, k2)

    if "удалить" == message.text.lower().split(' ')[0]: 
        AList.remove(message.text[8:])
        k4 = str(message.text[8:])
        index = k2.find(k4)
        q = len(k4) 
        q1 = index + q + 1
        k2 = k2[0:index] + k2[q1:]
        bot.send_message(message.chat.id, 'Готово, твоё аниме больше не в списке :)')
        bot.send_message(message.chat.id, k2)
    if message.text.lower() == "список":
        
        
        bot.send_message(message.chat.id, 'Вот твой список, братик: \n')
        bot.send_message(message.chat.id, k2)
    if message.text.lower() == "cколько у меня тайтлов":
        s = len(AList)
        print(s)
        bot.send_message(message.chat.id, s)
    if message.text.lower() == "погода":

        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
        params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()

        t ='Город: ' + str(s_city) + '\n' + 'Погодные условия: ' \
        + str(data['weather'][0]['description']) + '\n' \
        + 'Минимальная температура: ' + str(data['main']['temp_min']) \
        + '\n' + 'Максимальная температура: ' + str(data['main']['temp_max'])\
        + '\n' + 'Скорость ветра: ' + str(data['wind']['speed'])\
        + '\n' + 'Видимость: ' + str(data['visibility'])
        
        bot.send_message(message.chat.id,  t)
    if message.text.lower() == "погода на неделю":

        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
        params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()

        bot.send_message(message.chat.id,  'Прогноз погоды на неделю:')

        for i in data['list']:
            o = 'Дата: ' + str(i['dt_txt']) + '\nТемпература: ' + '{0:+3.0f}'.format(i['main']['temp'])\
            + '\nПогодные условия: ' + str(i['weather'][0]['description']) \
            + '\nСкорость ветра: ' + str(i['wind']['speed'])\
            + '\nВидимость: ' + str(i['visibility'])
            bot.send_message(message.chat.id,  o)
        
        
bot.infinity_polling()

# -*- coding: utf-8 -*-
import telebot;
TOKEN = '1420123353:AAH4y9RRjvPUgZOvht2QayuAHXK1_V3tJ4k'
bot = telebot.TeleBot(TOKEN);

from telebot.util import async_dec

from googlesearch import search
@async_dec()
def find_me(message, query):
    bot.send_message(message.chat.id, "Держи!")
    ## Google Search query results as a Python List of URLs
    search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))
    bot.send_message(message.chat.id, search_result_list[0])
    bot.send_message(message.chat.id, search_result_list[1])
    bot.send_message(message.chat.id, search_result_list[2])

with open("query.txt", "w") as f:
    f.write('Где живет енот')

@async_dec()
@bot.message_handler(commands=['request'])
def knowledge(message):
    bot.send_message(message.chat.id, "Спроси о чем-нибудь Енотю, и он пришлет полезные ссылочки об этом!")
    with open("query.txt", "w") as f:
        f.write('query')

from telebot import types
@async_dec()
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    with open('query.txt', 'r') as file:
        file_content=file.readlines()
        for line in file_content:
            ask = line.strip()
    if ask == "query":
        find_me(message, message.text)
        with open("query.txt", "w") as f:
            f.write('Где живет енот')


 bot.polling(none_stop=True, interval=0)

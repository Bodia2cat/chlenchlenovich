# -*- coding: UTF-8 -*-
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "1941291728:AAHtoTrH-wK9UGSV_ytnieDDdRjTnNDHTI4"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Привет! Меня зовут Член Залупович. Сейчас я мало что умею, но скоро это измениться. О бо мне посмотри в описании')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == "/getserver":
        res = requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.3:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]")
        await msg.answer(res.text)
        res = requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.4:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]")
        await msg.answer(res.text)
        res = requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.43:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]")
        await msg.answer(res.text)
        res = requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.44:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]")
        await msg.answer(res.text)
        res = requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.45:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]")
        await msg.answer(res.text)
        res = requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.45:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]")
        await msg.answer(res.text)
        res = requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.5:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]")
        await msg.answer(res.text)
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.59:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.61:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.107:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.109:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.166:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.171:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.172:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.173:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=185.169.134.174:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=80.66.82.191:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
        await msg.answer(requests.get("https://api.ip-games.ru/method/server.get?address=80.66.82.190:7777&key=[NZ6TTi0Vn9NZsT9mudmNqeNev6buJxLxOIRtC50r]"))
      if msg.text.lower() == '/sampchat':
         await msg.answer('Пока что эта функция не доступна, но скоро это будет исправленно')
      if msg.text.lower() == 'член':
         await msg.answer('Пиписька')
      if msg.text.lower() == 'залупович передай мне привет':
         await msg.answer('Салам хуйлапан на члене')
      if msg.text.lower() == 'залупович пошел нахуй':
         await msg.answer('А может ты пойдешь?')
      if msg.text.lower() == 'залупович ты даун':
         await msg.answer('Нет')
      if msg.text.lower() == 'Я ебал вас всех':
         await msg.answer('И я тебя')
      if msg.text.lower() == 'мать ебал':
         await msg.answer('Бан тебе нахуй')
      if msg.text.lower() == 'пошел нахуй':
         await msg.answer('А может ты пойдешь?')
      if msg.text.lower() == '/tagsadmins':
         await msg.answer('@krlnrnl - ||Цветочек')
         await msg.answer('@B_Votson - ||B_Votson')
         await msg.answer('@ell11ot - ||Господин Рэйв')
         await msg.answer('@typochelio - ||Votson')
    if msg.text.lower() == '/ЗОВ':
       await msg.answer('@krlnrnl, @typochelio, @ell11ot, @B_Votson || Вас вызвали старшие администраторы.')

if __name__ == '__main__':
   executor.start_polling(dp)
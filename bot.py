# -*- coding: UTF-8 -*-
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "1901906342:AAHbh1aVmvw80bInHqOUdLgRj7U2S4iTpNI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Привет! Меня зовут Юми. Сейчас я мало что умею, но скоро это измениться. О бо мне посмотри в описании')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    
    if msg.text.lower() == '/offabot':
        if msg.chat.id == 936106535:
            await msg.answer('Бот выключен. Для включения перезагрузите скрипт bot.py')
            exit()
        if msg.chat.id != 936106535:
           await msg.answer("Только разроботчик может полностю выключить скрипт!")
    if msg.text.lower() == '/outcode':
        if msg.chat.id == -1001288153166 or msg.chat.id == 936106535 or msg.chat.id == -1001248902740:
            await msg.answer('Исходный код бота вы всегда можете найти на сайте: github.com/Bodia2cat/https://github.com/Bodia2cat/chlenchlenovich')
    if msg.text.lower() == '/sampchat':
        await msg.answer('Пока что эта функция не доступна, но скоро это будет исправленно')
    if msg.text.lower() == '/tagsadmins':
        if msg.chat.id == -1001288153166 or msg.chat.id == 936106535 or msg.chat.id == -1001248902740:
            await msg.answer('@krlnrnl - ||Цветочек')
            await msg.answer('@B_Votson - ||B_Votson')
            await msg.answer('@ell11ot - ||Господин Рэйв')
            await msg.answer('@typochelio - ||Votson')
        if msg.text.lower() == '/зов':
         if msg.chat.id == -1001288153166 or msg.chat.id == 936106535 or msg.chat.id == -1001248902740:
               await msg.answer('@krlnrnl, @typochelio, @ell11ot, @B_Votson || Вас вызвали старшие администраторы.')
    if msg.text.lower() == '/зов':
        if msg.chat.id == -1001288153166 or msg.chat.id == 936106535 or msg.chat.id == -1001248902740:
            await msg.answer('@krlnrnl, @typochelio, @ell11ot, @B_Votson || Вас вызвали старшие администраторы.')
    if msg.text.lower() == "/chatid":
      cid = msg.chat.id
      await msg.answer(cid)
if __name__ == '__main__':
   executor.start_polling(dp)
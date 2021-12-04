from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (""" Assalomu alaykum! Ushbu bot:
    1) ingliz-o'zbek va aksincha tarzda matnlarni tarjima qilish;
    2) so'zning inglizcha talaffuzi(audio)sini jo'natish;
    3) yuborilgan so'zning ingliz va o'zbek tillaridagi ta'rif(definition)ini ko'rish;
    4) atama haqidagi to'liq ma'lumotni Wikipedia'dan izlash 
    kabi imkoniyatlarni beradi!

Marhamat, foydalanishingiz mumkin. Bismillahir Rohmanir Rohiym!""")

    
    await message.answer(text)

@dp.message_handler(commands='admin')
async def send_welcome(message: types.Message):
    
    await message.reply("""Dasturchi: Komilov Fotihbek
Manzil: @ProgerUzb
Boshqa loyihalar: @iProgs""")


from funksiya import get_definitions
from googletrans import Translator
from aiogram import types
from loader import dp
from filters.private_chat import IsPrivate
import wikipedia

from aiogram.types import Message, CallbackQuery, callback_query
from keyboards.inline.tarjimaKb import category, uzb
from keyboards.inline.callback_data import tarjima_callback


translator = Translator()

@dp.message_handler(IsPrivate())
async def tarjimon(message: types.Message):
    til = translator.detect(message.text).lang
    if len(message.text.split()) > 1:
        dest = 'uz' if til == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if til == 'en':
            word = message.text
            await message.answer(translator.translate(message.text, dest='uz').text)
        else:
            word = translator.translate(message.text, dest='en').text
            await message.answer(word)

        funk = get_definitions(word)

        if funk:
            global defin
            global wordfind
            wordfind = word[:]
            defin = f"Word: {word}\n<b>Definitions:</b>\n{funk['definitions']}" #f"<b>Word:</b> {word}\n<b>Definitions:</b>\n{funk['definitions']}"
            try:
                await message.reply_audio(funk['audio'])
            except:
                await message.reply("Audio topilmadi")
            
            await message.answer(defin, reply_markup=category)

                #await message.reply_audio(f"http://audio.linguarobot.io/en/{word.lower()}-us.mp3")
        else:
            await message.reply("Ushbu so'zning ta'rifi topilmadi!", reply_markup=category)


@dp.callback_query_handler(text='uzdef')
async def quron(call: CallbackQuery):
    await call.message.answer(translator.translate(defin, 'uz').text)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='wikifind')
async def sendwiki(call: CallbackQuery):
    try:
        wikipedia.set_lang('en')
        result = wikipedia.summary(wordfind)
        await call.message.answer(result, reply_markup=uzb)
        global natija
        natija = result[:]
    except:
        await call.message.answer('Bu mavzuga oid maqola topilmadi')
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='uzwiki')
async def uzwiki(call: CallbackQuery):
    await call.message.answer(translator.translate(natija, 'uz').text)
    await call.message.delete()
    await call.answer(cache_time=60)



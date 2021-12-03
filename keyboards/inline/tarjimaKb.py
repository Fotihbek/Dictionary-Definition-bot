from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard
from keyboards.inline import callback_data
from keyboards.inline.callback_data import tarjima_callback, wikiuz_callback

category = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ta'rif 🇺🇿", callback_data="uzdef"),
        InlineKeyboardButton(text='Wiki Find 🔍', callback_data="wikifind")

    ]])

uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="O'zbekcha 🇺🇿", callback_data="uzwiki") ]])
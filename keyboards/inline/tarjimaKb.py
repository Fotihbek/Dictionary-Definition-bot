from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard
from keyboards.inline import callback_data
from keyboards.inline.callback_data import tarjima_callback, wikiuz_callback

category = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ta'rif πΊπΏ", callback_data="uzdef"),
        InlineKeyboardButton(text='Wiki Find π', callback_data="wikifind")

    ]])

uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="O'zbekcha πΊπΏ", callback_data="uzwiki") ]])
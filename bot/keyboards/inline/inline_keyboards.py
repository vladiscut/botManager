from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def three_inline_buttons(list_but:list, row_width:tuple):
    ikb = InlineKeyboardBuilder()
    for b in list_but:
        ikb.button(text = str(b),callback_data=str(b))
    ikb.adjust(*row_width)
    return ikb.as_markup()
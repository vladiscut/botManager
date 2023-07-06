from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_reply_keyboard(list_but:list, row:tuple):
    rp_keyboard_builder = ReplyKeyboardBuilder()
    for but in list_but:
        rp_keyboard_builder.button(text=(but))
    # print(*row)
    rp_keyboard_builder.adjust(*row)
    return rp_keyboard_builder.as_markup(resize_keyboard=True,selective =True,one_time_keyboard= True )
    
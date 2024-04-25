from aiogram import types

from src.buttons.start import POPULAR_BUTTON, FIND_BUTTON

CREATE_BUTTON = 'Create recipe'
MY_RECIPES_BUTTON = 'See all my recipes'


def get_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=CREATE_BUTTON)],
        [types.KeyboardButton(text=POPULAR_BUTTON)],
        [types.KeyboardButton(text=FIND_BUTTON)],
        [types.KeyboardButton(text=MY_RECIPES_BUTTON)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb)

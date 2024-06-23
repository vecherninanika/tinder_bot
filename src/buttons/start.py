from aiogram import types


AUTH_BUTTON = 'Log in to add your own recipe'
POPULAR_BUTTON = 'View the most popular recipes'
FIND_BUTTON = 'Find recipe by ingredient'


def get_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=AUTH_BUTTON)],
        [types.KeyboardButton(text=POPULAR_BUTTON)],
        [types.KeyboardButton(text=FIND_BUTTON)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb)

from aiogram import types

LOGIN_BUTTON = 'Log in'
REGISTER_BUTTON = 'Register'


def get_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=LOGIN_BUTTON)],
        [types.KeyboardButton(text=REGISTER_BUTTON)]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb)

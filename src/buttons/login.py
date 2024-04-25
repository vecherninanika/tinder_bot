from aiogram import types

from src.buttons.auth import LOGIN_BUTTON


def get_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=LOGIN_BUTTON)]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb)

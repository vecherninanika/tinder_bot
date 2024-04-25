from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="👍",
            callback_data="like",
        )
    )
    return builder.as_markup()

from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MyCallback(CallbackData, prefix="my"):
    action: str
    recipe_id: int
    recipe_likes: int


def get_keyboard(recipe_id, recipe_likes) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="👍", callback_data=MyCallback(action='like', recipe_id=recipe_id, recipe_likes=recipe_likes).pack()
        )
    )
    return builder.as_markup()

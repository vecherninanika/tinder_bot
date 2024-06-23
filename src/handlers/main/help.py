from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from src.handlers.main.router import main_router

BOT_DESCRIPTION = 'In this bot you can: \n\
         - /register or /login \n\
         - Create your own recipe \n\
         - Search recipes by ingredients \n\
         - View the most popular recipes \n\
         You can see all possible actions in the keyboard.'


@main_router.message(
    Command(
        "help",
    )
)
async def help(message: types.Message, state: FSMContext):
    await message.answer(BOT_DESCRIPTION)

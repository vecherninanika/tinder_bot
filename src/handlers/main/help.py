from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from src.handlers.main.router import main_router


@main_router.message(Command("help",))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(
        'In this bot you can: \n\
         - Create your own recipe \n\
         - Search recipes by ingredients \n\
         - View the most popular recipes \n\
         Type "/menu" to see the list of possible commands.'
    )

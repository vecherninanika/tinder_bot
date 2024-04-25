from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from src.handlers.main.router import main_router
from src.buttons.start import get_keyboard
from src.state.login import LoginState


@main_router.message(Command("start",))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(LoginState.unauthorized)
    await message.answer('Welcome to our recipes bot!', reply_markup=get_keyboard())

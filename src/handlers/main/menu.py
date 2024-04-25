from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from src.handlers.main.router import main_router
from src.buttons.menu import get_keyboard
from src.state.login import LoginState


@main_router.message(Command("menu",))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(LoginState.unauthorized)
    await message.answer('Menu:', reply_markup=get_keyboard())

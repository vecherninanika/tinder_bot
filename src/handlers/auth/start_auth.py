from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.buttons.auth import get_keyboard, LOGIN_BUTTON, REGISTER_BUTTON
from src.buttons.start import AUTH_BUTTON
from src.handlers.auth.router import auth_router
from src.state.login import LoginState


@auth_router.message(F.text == AUTH_BUTTON, LoginState.unauthorized)
async def cmd_auth(message: types.Message):
    await message.answer('Register or log in into existing account', reply_markup=get_keyboard())


@auth_router.message(F.text == LOGIN_BUTTON, LoginState.unauthorized)
@auth_router.message(Command("login"))
async def login(message: types.Message, state: FSMContext):
    await state.set_state(LoginState.enter_code)
    await message.answer('Enter your personal code to log in')


@auth_router.message(F.text == REGISTER_BUTTON, LoginState.unauthorized)
@auth_router.message(Command("register"))
async def register(message: types.Message, state: FSMContext):
    await state.set_state(LoginState.create_code)
    await message.answer('Create a code to register')

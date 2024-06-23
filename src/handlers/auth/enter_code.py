import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from aiogram import types
from aiogram.fsm.context import FSMContext

from src.buttons.menu import get_keyboard
from conf.config import settings
from src.handlers.auth.router import auth_router
from src.state.login import LoginState
from src.utils.request import post_to_server


@auth_router.message(LoginState.enter_code)
async def enter_code(message: types.Message, state: FSMContext):
    print("ENTER CODE")

    code = message.text
    json = {
        'username': message.from_user.id,
        'code': code,
    }
    ok, response = await post_to_server('auth/login', json)

    if not ok:
        await message.answer(f"Error from server: {response.message}")
        return await state.set_state(LoginState.unauthorized)

    await state.set_data({'user_data': response})

    await state.set_state(LoginState.authorized)
    await message.answer("Successfully logged in.", reply_markup=get_keyboard())

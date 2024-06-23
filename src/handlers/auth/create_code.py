import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from aiogram import types
from aiogram.fsm.context import FSMContext

from src.buttons.login import get_keyboard
from conf.config import settings
from src.handlers.auth.router import auth_router
from src.state.login import LoginState
from src.utils.request import post_to_server


@auth_router.message(LoginState.create_code)
async def create_code(message: types.Message, state: FSMContext):
    print("CREATE CODE")
    code = message.text

    json = {
        'username': message.from_user.id,
        'code': code,
    }
    ok, response = await post_to_server('auth/register', json)

    if not ok:
        if response.code == 406:
            await message.answer(f"Your account already exists. /login")
        await message.answer(f"Error from server: {response.message}")
        return await state.set_state(LoginState.unauthorized)

    await message.answer("Registration complete.", reply_markup=get_keyboard())

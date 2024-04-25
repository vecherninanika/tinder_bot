import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from aiogram import types
from aiogram.fsm.context import FSMContext

from src.buttons.menu import get_keyboard
from conf.config import settings
from src.handlers.auth.router import auth_router
from src.state.login import LoginState


@auth_router.message(LoginState.enter_code)
async def enter_code(message: types.Message, state: FSMContext):
    print("ENTER CODE")

    code = message.text
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                        f'{settings.TINDER_BACKEND_HOST}/auth/login',
                        json={
                            'username': message.from_user.id,
                            'code': code,
                        },
            ) as response:
                response.raise_for_status()
                data = await response.json()
                print(data)
        except ClientResponseError:
            await message.answer("Your code is incorrect")
            await state.set_state(LoginState.unauthorized)
            return

    if data:
        await state.set_data({'user_data': data})

    await state.set_state(LoginState.authorized)
    await message.answer("Successfully logged in. Now you can:", reply_markup=get_keyboard())

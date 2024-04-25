import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from aiogram import types
from aiogram.fsm.context import FSMContext

from src.buttons.login import get_keyboard
from conf.config import settings
from src.handlers.auth.router import auth_router
from src.state.login import LoginState


# NOTE почему-то сюда не доходит
@auth_router.message(LoginState.create_code)
async def create_code(message: types.Message, state: FSMContext):
    print("CREATE CODE")
    code = message.text
    print(code)
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                        f'{settings.TINDER_BACKEND_HOST}/auth/register',
                        json={
                            'username': message.from_user.id,
                            'code': code,
                        },
            ) as response:
                response.raise_for_status()
                data = await response.json()
                print(data)
        except ClientResponseError:     # TODO if code already used
            await message.answer("Error")
            return

    await state.set_state(LoginState.unauthorized)
    await message.answer("Registration complete.", reply_markup=get_keyboard())

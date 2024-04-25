import aiohttp
from aiogram import types, F
from aiogram.fsm.context import FSMContext

from src.buttons.like_recipe import get_keyboard
from src.buttons.start import POPULAR_BUTTON
from conf.config import settings
from src.handlers.recipes.router import recipes_router


@recipes_router.message(F.text == POPULAR_BUTTON)
async def read_popular(message: types.Message, state: FSMContext):
    print("READ POPULAR")
    
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                    f'{settings.TINDER_BACKEND_HOST}/recipe/read_popular',
            ) as response:
                response.raise_for_status()
                data = await response.json()
                print(data)
        except aiohttp.ClientResponseError:
            return await message.answer("Error")

    if data:
        for recipe in data:
            await message.answer(recipe['title'], reply_markup=get_keyboard())
        return

    return await message.answer('Not found')

import aiohttp
from aiogram import types
from aiogram.fsm.context import FSMContext

from src.buttons.like_recipe import get_keyboard
from conf.config import settings
from src.handlers.recipes.router import recipes_router
from src.state.search import SearchState


@recipes_router.message(SearchState.type_ingredient)
async def type_ingredient(message: types.Message, state: FSMContext):
    print("TYPE INGREDIENT")

    ingredient = message.text
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                    f'{settings.TINDER_BACKEND_HOST}/recipe/find_by_ingredient',
                    params={'ingredient': ingredient}
            ) as response:
                response.raise_for_status()
                data = await response.json()
                print(data)
        except aiohttp.ClientResponseError as err:
            await message.answer(f"Error: {err}")
            return

    if data:
        await state.update_data({'recipe_data': data})
        answer_message = ", ".join([recipe['title'] for recipe in data])
        return await message.answer(answer_message, reply_markup=get_keyboard())

    return await message.answer('No recipes found')

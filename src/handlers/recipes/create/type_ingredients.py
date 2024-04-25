import logging
import aiohttp
from aiogram import F, types
from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.handlers.recipes.router import recipes_router
from src.state.create import CreateState


@recipes_router.callback_query(CreateState.type_ingredients)
async def type_ingredients(message: types.Message, state: FSMContext):
    text = message.text
    ingredients = text.split('\n')
    data = await state.get_data()
    recipe_title = data['recipe_title']
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                    f'{settings.TINDER_BACKEND_HOST}/recipe/create',
                    params={'title': updated_likes}
            ) as response:
                data = await response.json()
                response.raise_for_status()
        except Exception:
            logging.exception(f'Error adding like')
    await callback.message.delete()

    await state.set_state(CreateState.type_ingredients)


import logging
import aiohttp
from aiogram import F, types
from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.handlers.recipes.router import recipes_router


@recipes_router.callback_query(F.data == 'like')
async def add_like(callback: types.CallbackQuery, state: FSMContext):
    print("ADD LIKE")
    
    data = await state.get_data()
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            recipe_id = data['recipe_data']['id']
            updated_likes = data['recipe_data']['likes'] + 1
            async with session.post(
                    f'{settings.TINDER_BACKEND_HOST}/recipe/update/{recipe_id}',
                    params={'likes': updated_likes}
            ) as response:
                data = await response.json()
                response.raise_for_status()
        except Exception:
            logging.exception(f'Error adding like')
    await callback.message.delete()

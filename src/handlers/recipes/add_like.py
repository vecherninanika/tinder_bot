import logging
import aiohttp
from aiogram import F, types
from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.handlers.recipes.router import recipes_router
from src.utils.request import post_to_server
from src.buttons.like_recipe import MyCallback


@recipes_router.callback_query(MyCallback.filter(F.action == "like"))
async def add_like(message: types.Message, callback_data: MyCallback):
    print("ADD LIKE")

    recipe_id = callback_data.recipe_id
    updated_likes = callback_data.recipe_likes + 1
    json = {'likes': updated_likes}
    ok, response = await post_to_server(f'recipe/update/{recipe_id}', json)

    if not ok:
        return await message.answer(f"Error from server: {response.message}")

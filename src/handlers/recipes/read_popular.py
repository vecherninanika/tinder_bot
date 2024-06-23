import aiohttp
from aiogram import types, F
from aiogram.fsm.context import FSMContext

from src.buttons.like_recipe import get_keyboard
from src.buttons.start import POPULAR_BUTTON
from conf.config import settings
from src.handlers.recipes.router import recipes_router
from src.utils.request import get_from_server


@recipes_router.message(F.text == POPULAR_BUTTON)
async def read_popular(message: types.Message, state: FSMContext):
    print("READ POPULAR")

    ok, response = await get_from_server('recipe/read_popular')

    if not ok:
        return await message.answer(f"Error from server: {response.message}")

    if response is []:
        return await message.answer('There are no recipes yet.', reply_markup=get_keyboard())

    for recipe in response:
        title = recipe['title']
        ingredients = ", ".join(recipe['ingredients'])
        answer = f'{title} \nIngredients: {ingredients}'

        await message.answer(answer, reply_markup=get_keyboard(recipe['id'], recipe['likes']))

    return

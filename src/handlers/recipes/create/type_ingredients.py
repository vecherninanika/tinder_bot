import logging
import aiohttp
from aiogram import F, types
from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.handlers.recipes.router import recipes_router
from src.state.recipe import CreateState
from src.state.login import LoginState
from src.utils.request import post_to_server
from src.buttons.menu import get_keyboard


@recipes_router.message(CreateState.type_ingredients)
async def type_ingredients(message: types.Message, state: FSMContext):
    text = message.text
    ingredients = text.split('\n')
    data = await state.get_data()
    recipe_title = data['new_recipe_title']

    json = {"title": recipe_title, "ingredients": ingredients, "username": message.from_user.id}

    ok, response = await post_to_server('recipe/create', params=json)

    if not ok:
        return await message.answer(f"Error from server: {response.message}")

    await state.set_state(LoginState.authorized)

    await message.answer('Recipe created. You can now see it in "My recipes".', reply_markup=get_keyboard())

import aiohttp
from aiogram import types, F
from aiogram.fsm.context import FSMContext

from src.buttons.like_recipe import get_keyboard
from src.buttons.menu import MY_RECIPES_BUTTON
from conf.config import settings
from src.handlers.recipes.router import recipes_router
from src.state.login import LoginState
from src.utils.request import get_from_server


@recipes_router.message(F.text == MY_RECIPES_BUTTON, LoginState.authorized)
async def read_user_recipes(message: types.Message, state: FSMContext):
    print("READ USER RECIPES")

    data = await state.get_data()
    user_id = data['user_data']['user_id']

    ok, response = await get_from_server(f'recipe/read_user_recipes/{user_id}')

    if not ok:
        if response.code == 404:
            return await message.answer("You do not have any recipes yey", reply_markup=get_keyboard())
        return await message.answer(f'Error from server: {response.message}', reply_markup=get_keyboard())

    if not response:
        return await message.answer('You do not have recipes yet.', reply_markup=get_keyboard())

    for recipe in response:
        title = recipe['title']
        ingredients = ", ".join(recipe['ingredients'])
        answer = f'{title} \nIngredients: {ingredients}'
        await message.answer(answer, reply_markup=get_keyboard())

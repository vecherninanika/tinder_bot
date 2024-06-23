from aiogram import F, types
from aiogram.fsm.context import FSMContext

from src.handlers.recipes.router import recipes_router
from src.state.recipe import CreateState


@recipes_router.message(CreateState.type_recipe)
async def type_recipe(message: types.Message, state: FSMContext):
    recipe_title = message.text
    await state.update_data({'new_recipe_title': recipe_title})
    await state.set_state(CreateState.type_ingredients)
    await message.answer('Type the ingredients, each on a new line.')

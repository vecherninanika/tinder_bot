from aiogram import F, types
from aiogram.fsm.context import FSMContext

from src.handlers.recipes.router import recipes_router
from src.state.create import CreateState


@recipes_router.callback_query(CreateState.type_recipe)
async def type_recipe(message: types.Message, state: FSMContext):
    recipe_title = message.text
    await state.update_data({'recipe_title': recipe_title})
    await state.set_state(CreateState.type_ingredients)
    await message.answer('Type the ingredients, each on the next line.')

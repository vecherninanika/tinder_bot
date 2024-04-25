from aiogram import types, F
from aiogram.fsm.context import FSMContext

from src.buttons.menu import CREATE_BUTTON
from src.handlers.recipes.router import recipes_router
from src.state.create import CreateState


@recipes_router.message(F.text == CREATE_BUTTON)
async def start_search(message: types.Message, state: FSMContext):
    await state.set_state(CreateState.type_recipe)
    await message.answer('Enter the title of your recipe')

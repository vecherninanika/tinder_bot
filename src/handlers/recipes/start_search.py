from aiogram import types, F
from aiogram.fsm.context import FSMContext

from src.buttons.start import FIND_BUTTON
from src.handlers.auth.router import auth_router
from src.state.search import SearchState


@auth_router.message(F.text == FIND_BUTTON)
async def start_search(message: types.Message, state: FSMContext):
    print("START SEARCH")
    
    await state.set_state(SearchState.type_ingredient)
    await message.answer('Type an ingredient to find recipes with it')

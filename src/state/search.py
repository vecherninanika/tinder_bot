from aiogram.fsm.state import StatesGroup, State


class SearchState(StatesGroup):
    type_ingredient = State()

    popular_recipes = State()

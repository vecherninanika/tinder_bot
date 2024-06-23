from aiogram.fsm.state import StatesGroup, State


class CreateState(StatesGroup):
    type_recipe = State()

    type_ingredients = State()


class SearchState(StatesGroup):
    type_ingredient = State()

    popular_recipes = State()

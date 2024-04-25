from aiogram.fsm.state import StatesGroup, State


class CreateState(StatesGroup):
    type_recipe = State()

    type_ingredients = State()

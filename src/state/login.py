from aiogram.fsm.state import StatesGroup, State


class LoginState(StatesGroup):
    unauthorized = State()

    enter_code = State()

    enter_name = State()

    create_code = State()

    authorized = State()

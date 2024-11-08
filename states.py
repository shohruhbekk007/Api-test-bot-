from aiogram.fsm.state import State, StatesGroup

class QoshishState(StatesGroup):
    name = State()
    url = State()
    finish = State()
from aiogram.fsm.state import State, StatesGroup

class questionStates(StatesGroup):
    question_send = State()
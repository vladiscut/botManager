from aiogram.fsm.state import State, StatesGroup

class orderStates(StatesGroup):
    adress = State()
    number = State()
    send_chat = State()
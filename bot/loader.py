from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

tech_chat = '-998130772'

token = 'your_token'

ADMIN = ['344150886',]

bot = Bot(token=token, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher()

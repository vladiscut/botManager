import asyncio
from aiogram.filters import Command
from loader import dp, bot
from utils.set_bot_commands import set_default_commands
# from connectors.db_funct import create_table
from handlers.start_command import *
from states.order_states import orderStates
from aiogram import F


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(bot)
    print('Bot Started!')

async def start():
    # dp.message.register(process_main_menu_command,Command(commands=['catalogue']))
    # dp.message.register(process_main_menu_command,F.text=='Главное меню')
    dp.startup.register(on_startup)
    dp.message.register(start_command,Command(commands=['start']))
    dp.message.register(start_command,F.text=='Обратно в меню')
    dp.callback_query.register(newquestion,F.data.startswith('Задать вопрос'))
    dp.message.register(get_id_command,Command(commands=['getid']))
    dp.message.register(otvet,Command(commands=['ответ']))
    dp.message.register(dop_data,Command(commands=['допинфо']))
    dp.message.register(newquestion_send,questionStates.question_send)
    # dp.message.register(neworder,FSMQuestion.text)
    # try:
    await dp.start_polling(bot, skip_updates=True)
    # finally:
    #     await bot.session.close()

if __name__ == '__main__':
    # create_table()
    asyncio.run(start())


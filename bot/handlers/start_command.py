from aiogram import types
from loader import dp,bot,ADMIN,tech_chat
from aiogram.fsm.context import FSMContext
from keyboards.inline.inline_keyboards import *
from keyboards.reply.reply_keyboards import *
from states.question_states import questionStates
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")



channel_id = '-1001780286274'


#админ функция ответа
async def otvet(msg: types.Message):
    chat_id = str(msg.text).split(' ')[1]
    answer = ''
    answer_raw = str(msg.text).split(' ')[2:]
    photo1 = types.InputMediaPhoto(type='photo', media=types.FSInputFile(r'photos/example1.jpg'), caption='Пример копирования')
    photo2 = types.InputMediaPhoto(type='photo', media=types.FSInputFile(r'photos/example2.jpg'), caption='Пример отправки')
    media=[photo2,photo1]
    await bot.send_media_group(chat_id, media)
    for w in answer_raw:
        answer += w + ' '
    try:
        await bot.send_message(chat_id, f"✉ Новое уведомление!\nОтвет от тех.поддержки:\n\n`{str(answer)}`\n\n📝 Чтобы ответить введите `/допинфо Ваш ответ`",parse_mode='Markdown')
    except:
        await bot.send_message(chat_id, f"✉ Новое уведомление!\nОтвет от тех.поддержки:\n\n`{str(answer)}`\n\n📝 Чтобы ответить введите `/допинфо Ваш ответ`")
    await msg.reply('✅ Ответ отправлен пользователю!')

#клиент функция доп_инфы
async def dop_data(msg: types.Message):
    answer = ''
    answer_raw = str(msg.text).split(' ')[1:]
    for w in answer_raw:
        answer += w + ' '
    try:
        await bot.send_message(tech_chat, f"✉ | Уточнение\nОт: {msg.chat.username}\n\nТекст:\n\n`{str(answer)}`\n\n📝 Чтобы ответить введите `/ответ {msg.chat.id} Ваш ответ`", parse_mode='Markdown')
    except:
        await bot.send_message(tech_chat, f"✉ | Уточнение\nОт: {msg.chat.username}\n\nТекст:\n\n`{str(answer)}`\n\n📝 Чтобы ответить введите `/ответ {msg.chat.id} Ваш ответ`")
    await msg.answer(f"Уточнение отправлено, спасибо!✅")


#функция для получения ID
async def get_id_command(msg: types.Message):
      await bot.send_message(chat_id= msg.chat.id,
                        text=msg.chat.id)

#start 
async def start_command(msg: types.Message, state: FSMContext):
      await state.clear()
      kb = three_inline_buttons(['Задать вопрос',],(1,))
      await bot.send_message(chat_id= msg.chat.id,
                        text='Привет 👋\nТы перешёл в Бот-менеджер MarketBuyer😋\nВыбери нужный пункт по кнопке ниже👇',
                        reply_markup=kb)



### ФУНКЦИИ ВОПРОСА ###      
async def newquestion(call: types.CallbackQuery, state: FSMContext):
      kb = get_reply_keyboard(['Обратно в меню',],(1,))
      await bot.send_message(chat_id= call.message.chat.id,
                  text='Здесь ты можешь задать любой вопрос, касающийся нашей работы👐\nОтправь номер телефона для связи и свой вопрос, первый освободившийся оператор ответит тебе ASAP.✍️\nПример `89001234567, заказал 9кг. огурцов, когда придут?`, нажми чтобы скопировать шаблон',
                  reply_markup=kb, parse_mode='Markdown')
      
      await state.set_state(questionStates.question_send)

async def newquestion_send(msg: types.Message, state: FSMContext):
      print(msg.text)
      question = msg.text
      await bot.send_message(tech_chat, f"✉ | Новый вопрос\nОт: {msg.chat.username}\nВопрос: `{question}`\n\n📝 Чтобы ответить на вопрос введите `/ответ {msg.chat.id} Ваш ответ`",
							   parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove)
      await msg.answer(f"Ваш вопрос отправлен в поддержку, модератор скоро ответит вам в этом чате✅")
      await state.clear()
### КОНЕЦ ФУНКЦИЙ ВОПРОСА ###





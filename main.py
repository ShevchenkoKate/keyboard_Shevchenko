from main import bot, dp
from aiogram import types
from aiogram.types import Messege

keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

array_keyboard = ['Button1', 'Button2']

async def send_to_admin(dp):
    await bot.send.messege(chat_id=155752773, text="Bot start")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text='Hello', reply_markup=keyboard_markup)

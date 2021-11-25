from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu
from loader import dp
from utils.db_api import database as db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await db.get_user(user_id=message.from_user.id)
    if user:
        markup = await menu(user)
        await message.answer(f"Salom, {message.from_user.full_name}!\n")
        await message.answer("Car Service botiga xush kelibsiz", reply_markup=markup)
    else:
        user = await db.add_user(user_id=message.from_user.id, name=message.from_user.full_name)
        markup = await menu(user)
        await message.answer(f"Salom, {message.from_user.full_name}!\n")
        await message.answer("Car Service botiga xush kelibsiz", reply_markup=markup)


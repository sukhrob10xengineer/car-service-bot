import typing

from . import base
from . import fields
from .message import Message
from .user import User

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ContentTypes, ReplyKeyboardRemove

from backend.models import Order
from keyboards.default.cartype import menuType
from keyboards.default.menu import menu, contact_btn
from keyboards.inline.main_inline import main_callback_data, confirm_btn, start_anketa_btn
from utils.db_api.database import get_user
from keyboards.inline.main_inline import time_control_btn
from loader import dp, bot


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    user = await get_user(user_id=message.from_user.id)
    if user:
        markup = await menu(user)
        await message.answer("Service turini tanlang", reply_markup=markup)
    else:
        await message.answer("Serverda xatolik mavjud. /start")


@dp.message_handler(text="🛠Bizning servislar")
async def send_link(message: Message):
    await message.answer("Servis turini tanlang", reply_markup=menuType)


@dp.message_handler(text="🔙Ortga")
async def send_link(message: Message):
    user = await get_user(user_id=message.from_user.id)
    if user:
        markup = await menu(user)
        await message.answer("Service turini tanlang", reply_markup=markup)


@dp.message_handler(text="🗺Bizning manzil")
async def send_link(message: Message):
    await message.answer("🗺Lokatsiya: https://goo.gl/maps/TttmVbCShzxQmTK37")


@dp.message_handler(text="🔧Muntazam parvarishlash")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Anketani to'ldiring va sizga qulay bo'lgana vaqtni tanlang\n"
                         "\n"
                         "Bu servisning narxi: 150.000 s'om", reply_markup=start_anketa_btn)


@dp.message_handler(text="🚘Yangi va eski avtomobillarni tayyorlash va sotish")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Anketani to'ldiring va sizga qulay bo'lgana vaqtni tanlang\n"
                         "\n"
                         "Bu servisning narxi: 150.000 s'om", reply_markup=start_anketa_btn)



@dp.message_handler(text="🕹Avtomatik va mexanik uzatmalarni ta'mirlash")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Anketani to'ldiring va sizga qulay bo'lgana vaqtni tanlang\n"
                         "\n"
                         "Bu servisning narxi: 150.000 s'om", reply_markup=start_anketa_btn)



@dp.message_handler(text="🏎Dvigatellarga texnik xizmat ko'rsatish va ta'mirlash")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Anketani to'ldiring va sizga qulay bo'lgana vaqtni tanlang\n"
                         "\n"
                         "Bu servisning narxi: 150.000 s'om", reply_markup=start_anketa_btn)



@dp.message_handler(text="🎨Avtomobil tanasini tuzatish")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Anketani to'ldiring va sizga qulay bo'lgana vaqtni tanlang\n"
                         "\n"
                         "Bu servisning narxi: 150.000 s'om", reply_markup=start_anketa_btn)



@dp.message_handler(text="🪛Avtomobillarda elektr jihozlarini ta'mirlash")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Anketani to'ldiring va sizga qulay bo'lgana vaqtni tanlang\n"
                         "\n"
                         "Bu servisning narxi: 150.000 s'om", reply_markup=start_anketa_btn)



@dp.message_handler(text="🚙Avtomobillar va ehtiyot qismlarni tiklash")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Anketani to'ldiring va sizga qulay bo'lgana vaqtni tanlang\n"
                         "\n"
                         "Bu servisning narxi: 150.000 s'om", reply_markup=start_anketa_btn)



@dp.message_handler(text="🚀Tashqi va ichki tuning")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Anketani to'ldiring va sizga qulay bo'lgana vaqtni tanlang\n"
                         "\n"
                         "Bu servisning narxi: 150.000 s'om", reply_markup=start_anketa_btn)



@dp.callback_query_handler(text="go_anketa")
async def start_anketa(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.message.answer("Iltimos to'liq ismingizni kiriting")
    await state.set_state("fullname")


@dp.callback_query_handler(text="back_to_services")
async def back_to_services_fun(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Servis turini tanlang", reply_markup=menuType)




@dp.message_handler(state="fullname")
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Iltimos telefon raqamingizni kiriting", reply_markup=contact_btn)
    await state.set_state("phone")


@dp.message_handler(state="phone", content_types=ContentTypes.CONTACT)
async def get_car(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    await state.update_data(phone=phone)
    await message.answer("Iltimos avtomobil markasini kiriting",reply_markup=ReplyKeyboardRemove(True))
    await state.set_state("car_name")


@dp.message_handler(state="car_name")
async def diwndiwdnw(message: Message, state: FSMContext):
    car_name = message.text
    await state.update_data(car_name=car_name)
    await message.answer("Iltimos qulay vaqtni tanlang", reply_markup=time_control_btn)
    await state.set_state("cartime")


@dp.callback_query_handler(main_callback_data.filter(), state="cartime")
async def get_time_and_confirm(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    cartime = callback_data.get("cartime")
    await state.update_data(cartime=cartime)
    await call.message.edit_reply_markup()
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    car_name = data.get("car_name")
    text = f"""
Ism: {name}

Telfon: {phone}

Mashina turi: {car_name}

Vaqti: {cartime}
"""
    car_order = Order()
    car_order.servic_type = "🔧Muntazam parvarishlash"
    car_order.full_name = name
    car_order.phone_num = phone
    car_order.car_name = car_name
    car_order.cartime = cartime
    car_order.payment = False

    car_order.save()


    await call.message.answer(text, reply_markup=confirm_btn)

    await state.set_state("confirm_or_cancel")



@dp.callback_query_handler(main_callback_data.filter(), state="cartime")
async def get_time_and_confirm(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    cartime = callback_data.get("cartime")
    await state.update_data(cartime=cartime)
    await call.message.edit_reply_markup()
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    car_name = data.get("car_name")
    text = f"""
Ism: {name}

Telfon: {phone}

Mashina turi: {car_name}

Vaqti: {cartime}
"""
    car_order = Order()
    car_order.servic_type = "🚘Yangi va eski avtomobillarni tayyorlash va sotish"
    car_order.full_name = name
    car_order.phone_num = phone
    car_order.car_name = car_name
    car_order.cartime = cartime
    car_order.payment = False

    car_order.save()

    await call.message.answer(text, reply_markup=confirm_btn)

    await state.set_state("confirm_or_cancel")


@dp.callback_query_handler(text="cancel")
async def back_to_services_fun(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Servis turini tanlang", reply_markup=menuType)

 





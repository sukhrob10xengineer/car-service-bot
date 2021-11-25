from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def menu(user):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if user.user_type == "ADMIN":
        markup.row(KeyboardButton(text="🛠Bizning servislar"),KeyboardButton(text="ADMIN"))

    markup.row(KeyboardButton(text="🛠Bizning servislar"))
    markup.row(KeyboardButton(text="🗺Bizning manzil", request_location=True),KeyboardButton(text="🌐Biz haqimizda"))
    markup.row(
        KeyboardButton(text="⚙️Moslamalar"),
        KeyboardButton(text="📞Biz bilan bo'glanish")
    )

    return markup


contact_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telfon raqamni kiritig", request_contact=True)
        ]
    ],
    resize_keyboard=True
)
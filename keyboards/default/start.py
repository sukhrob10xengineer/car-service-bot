from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛠Bizning servislar"),
        ],
        [
            KeyboardButton(text="🗺Bizning manzil"),
            KeyboardButton(text="🌐Biz haqimizda"),
        ],
        [
            KeyboardButton(text="⚙️Moslamalar"),
            KeyboardButton(text="📞Biz bilan bo'glanish")
        ]
    ],
    resize_keyboard=True
)

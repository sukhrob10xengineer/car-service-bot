from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuType = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔧Muntazam parvarishlash"),
            KeyboardButton(text="🚘Yangi va eski avtomobillarni tayyorlash va sotish"),

        ],
        [
            KeyboardButton(text="🕹Avtomatik va mexanik uzatmalarni ta'mirlash"),
            KeyboardButton(text="🏎Dvigatellarga texnik xizmat ko'rsatish va ta'mirlash"),
        ],
        [
            KeyboardButton(text="🎨Avtomobil tanasini tuzatish"),
            KeyboardButton(text="🪛Avtomobillarda elektr jihozlarini ta'mirlash")
        ],
        [
            KeyboardButton(text="🚙Avtomobillar va ehtiyot qismlarni tiklash"),
            KeyboardButton(text="🚀Tashqi va ichki tuning "),
        ],
        [
            KeyboardButton(text="🔙Ortga",)
        ]
    ],
    resize_keyboard = True
)
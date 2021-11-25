import os

import django


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "admin.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})

    django.setup()


async def on_startup(dispatcher):
    from utils.notify_admins import on_startup_notify
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    setup_django()

    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)

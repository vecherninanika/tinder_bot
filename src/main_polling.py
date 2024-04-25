import asyncio

from aiogram.types import BotCommand

from src.integrations.tg_bot import get_dispatcher, get_tg_bot
from src.logger import logger
from src.on_startup.logger import setup_logger


async def start_polling() -> None:
    bot = get_tg_bot()
    dp = get_dispatcher()
    await bot.set_my_commands(
        [
            BotCommand(command='start', description='Start bot'),
            BotCommand(command='help', description='Log in'),
            BotCommand(command='menu', description='Log in'),
            BotCommand(command='register', description='Register'),
            BotCommand(command='login', description='Log in'),
        ]
    )

    await bot.delete_webhook()
    logger.info('Deleted webhook')

    setup_logger()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_polling())

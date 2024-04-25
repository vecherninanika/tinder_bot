from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from src.handlers.auth.router import auth_router
from src.handlers.main.router import main_router
from src.handlers.recipes.router import recipes_router
from src.integrations.redis import redis
from src.middleware.logger import LogMessageMiddleware


def setup_dispatcher(bot: Bot) -> Dispatcher:
    storage = RedisStorage(redis)
    dp = Dispatcher(storage=storage, bot=bot)

    dp.include_routers(main_router)
    dp.include_routers(auth_router)
    dp.include_routers(recipes_router)

    dp.message.middleware(LogMessageMiddleware())
    dp.callback_query.middleware(LogMessageMiddleware())

    return dp

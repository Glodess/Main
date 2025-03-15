from aiogram.client.session.aiohttp import AiohttpSession
session = AiohttpSession(proxy='http://proxy.server:3128')
import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


API_TOKEN = '7561819834:AAEdIF0tTVBI5QP5-y5iGMSaYiqqrN_Cp8E'

proxy_url = 'http://proxy.server:3128'
bot = Bot(token=API_TOKEN,proxy=proxy_url, session=session)

WEBHOOK_HOST = 'https://www.pythonanywhere.com'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = 443

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    return SendMessage(message.chat.id, message.text)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

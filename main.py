from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

import messages
from user_input import UserInput

load_dotenv()

bot = Bot(
    token=os.getenv('BOT_TOKEN'),
    parse_mode="HTML"
)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome_message(message: types.Message):
    await message.answer(messages.welcome)


@dp.message_handler(commands=['about'])
async def about_message(message: types.Message):
    await message.answer(messages.about)


@dp.message_handler()
async def process_user_input(message: types.Message):
    result = UserInput().get_translation(message.text)
    if result:
        await message.answer(result)
    else:
        await message.answer(messages.fail_repeat)


if __name__ == "__main__":
    executor.start_polling(dp)

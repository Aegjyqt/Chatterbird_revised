from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

import messages

load_dotenv()

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome_message(message: types.Message):
    await message.answer(messages.welcome)

@dp.message_handler(commands=['about'])
async def welcome_message(message: types.Message):
    await message.answer(messages.about)



if __name__ == "__main__":
    executor.start_polling(dp)

from aiogram.types import Message
from aiogram.filters import Command, CommandStart


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Отправь мне input.csv файл')


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text='Отправь мне input.csv файл')
